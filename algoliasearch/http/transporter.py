from asyncio import TimeoutError
from typing import Optional, Union
from urllib.parse import urlencode

from aiohttp import ClientSession, TCPConnector
from async_timeout import timeout

from algoliasearch.http.api_response import ApiResponse
from algoliasearch.http.base_config import BaseConfig
from algoliasearch.http.exceptions import (
    AlgoliaUnreachableHostException,
    RequestException,
)
from algoliasearch.http.request_options import RequestOptions
from algoliasearch.http.retry import RetryOutcome, RetryStrategy
from algoliasearch.http.serializer import QueryParametersSerializer
from algoliasearch.http.verb import Verb


class Transporter:
    def __init__(self, config: BaseConfig) -> None:
        self._config = config
        self._retry_strategy = RetryStrategy()
        self._session = ClientSession(
            connector=TCPConnector(use_dns_cache=False), trust_env=True
        )

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

    async def request(
        self,
        verb: Verb,
        path: str,
        data: Optional[Union[dict, list]],
        request_options: RequestOptions,
        use_read_transporter: bool,
    ) -> ApiResponse:
        query_parameters = dict(request_options.query_parameters)

        if verb == Verb.GET or use_read_transporter:
            self._timeout = request_options.timeouts["read"]
            hosts = self._config.hosts.read()
            query_parameters.update(request_options.data)
        else:
            self._timeout = request_options.timeouts["write"]
            hosts = self._config.hosts.write()

        if isinstance(data, dict):
            data.update(request_options.data)

        if len(query_parameters) > 0:
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

        for host in self._retry_strategy.valid_hosts(hosts):
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

                    response = ApiResponse(
                        verb=verb,
                        url=url,
                        status_code=resp.status,
                        headers=resp.headers,
                        raw_data=await resp.text(),
                        error_message=str(resp.reason),
                    )

            except TimeoutError as e:
                response = ApiResponse(error_message=str(e), is_timed_out_error=True)

            decision = self._retry_strategy.decide(host, response)

            if decision == RetryOutcome.SUCCESS:
                return response
            elif decision == RetryOutcome.FAIL:
                content = response.error_message
                if response.data and "message" in response.data:
                    content = response.content["message"]

                raise RequestException(content, response.status_code)

        raise AlgoliaUnreachableHostException("Unreachable hosts")


class EchoTransporter(Transporter):
    def __init__(self, config: BaseConfig) -> None:
        self._config = config

    async def request(
        self,
        verb: Verb,
        path: str,
        data: Optional[Union[dict, list]],
        request_options: RequestOptions,
        use_read_transporter: bool,
    ) -> ApiResponse:
        return ApiResponse(
            verb=verb,
            path=path,
            status_code=200,
            query_parameters=QueryParametersSerializer(
                query_parameters=request_options.query_parameters
            ).query_parameters,
            headers=dict(request_options.headers),
            raw_data=data,
        )
