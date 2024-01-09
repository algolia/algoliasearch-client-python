from asyncio import TimeoutError
from json import loads
from typing import Any, Dict, List, Optional, Union
from urllib.parse import urlencode

from aiohttp import ClientSession, TCPConnector
from async_timeout import timeout

from algoliasearch.http.api_response import ApiResponse
from algoliasearch.http.base_config import BaseConfig
from algoliasearch.http.exceptions import (
    AlgoliaUnreachableHostException,
    RequestException,
)
from algoliasearch.http.hosts import Host
from algoliasearch.http.request_options import RequestOptions
from algoliasearch.http.retry import RetryOutcome, RetryStrategy
from algoliasearch.http.serializer import QueryParametersSerializer
from algoliasearch.http.verb import Verb


class Transporter:
    _config: BaseConfig
    _retry_strategy: RetryStrategy
    _session: ClientSession
    _hosts: List[Host]

    def __init__(self, config: BaseConfig) -> None:
        self._config = config
        self._retry_strategy = RetryStrategy()
        self._session = None

    async def __aenter__(self) -> None:
        return self

    async def __aexit__(self, exc_type, exc_value, traceback) -> None:
        await self.close()

    async def close(self) -> None:
        if self._session is not None:
            session = self._session
            self._session = None

            await session.close()

    def __enter__(self) -> None:
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        pass

    def prepare(
        self,
        request_options: RequestOptions,
        use_read_transporter: bool,
    ) -> Dict[str, Any]:
        query_parameters = dict(request_options.query_parameters)

        if use_read_transporter:
            self._timeout = request_options.timeouts["read"]
            self._hosts = self._config.hosts.read()
            query_parameters.update(request_options.data)

            return query_parameters

        self._timeout = request_options.timeouts["write"]
        self._hosts = self._config.hosts.write()

    async def request(
        self,
        verb: Verb,
        path: str,
        data: Optional[Union[dict, list]],
        request_options: RequestOptions,
        use_read_transporter: bool,
    ) -> ApiResponse:
        if self._session is None:
            self._session = ClientSession(
                connector=TCPConnector(use_dns_cache=False), trust_env=True
            )

        query_parameters = self.prepare(
            request_options, verb == Verb.GET or use_read_transporter
        )

        if isinstance(data, dict):
            data.update(request_options.data)

        if query_parameters is not None and len(query_parameters) > 0:
            path = "{}?{}".format(
                path,
                urlencode(
                    sorted(
                        QueryParametersSerializer(
                            query_parameters=query_parameters
                        ).query_parameters.items(),
                        key=lambda val: val[0],
                    )
                ),
            )

        for host in self._retry_strategy.valid_hosts(self._hosts):
            url = "https://{}{}".format(host.url, path)

            proxy = None
            if url.startswith("https"):
                proxy = self._config.proxies.get("https")
            elif url.startswith("http"):
                proxy = self._config.proxies.get("http")

            try:
                async with timeout(self._timeout):
                    resp = await self._session.request(
                        method=verb,
                        url=url,
                        headers=request_options.headers,
                        data=data,
                        proxy=proxy,
                    )

                    _raw_data = await resp.text()
                    response = ApiResponse(
                        verb=verb,
                        path=path,
                        url=url,
                        host=host.url,
                        status_code=resp.status,
                        headers=resp.headers,
                        data=_raw_data,
                        raw_data=_raw_data,
                        error_message=str(resp.reason),
                    )

            except TimeoutError as e:
                response = ApiResponse(
                    verb=verb,
                    path=path,
                    url=url,
                    host=host.url,
                    error_message=str(e),
                    is_timed_out_error=True,
                )

            decision = self._retry_strategy.decide(host, response)

            if decision == RetryOutcome.SUCCESS:
                return response
            elif decision == RetryOutcome.FAIL:
                content = response.error_message
                if response.data and "message" in response.data:
                    content = loads(response.data)["message"]

                raise RequestException(content, response.status_code)

        raise AlgoliaUnreachableHostException("Unreachable hosts")


class EchoTransporter(Transporter):
    def __init__(self, config: BaseConfig) -> None:
        self._config = config
        self._retry_strategy = RetryStrategy()

    async def request(
        self,
        verb: Verb,
        path: str,
        data: Optional[Union[dict, list]],
        request_options: RequestOptions,
        use_read_transporter: bool,
    ) -> ApiResponse:
        self.prepare(request_options, verb == Verb.GET or use_read_transporter)

        return ApiResponse(
            verb=verb,
            path=path,
            status_code=200,
            host=self._retry_strategy.valid_hosts(self._hosts)[0].url,
            timeouts={
                "connect": request_options.timeouts["connect"],
                "response": self._timeout,
            },
            query_parameters=QueryParametersSerializer(
                query_parameters=request_options.query_parameters
            ).query_parameters,
            headers=dict(request_options.headers),
            data=data,
            raw_data=data,
        )
