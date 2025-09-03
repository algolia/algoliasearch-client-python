from asyncio import TimeoutError
from json import loads
from typing import List, Optional

from aiohttp import ClientSession, TCPConnector
from async_timeout import timeout

from algoliasearch.http.api_response import ApiResponse
from algoliasearch.http.base_config import BaseConfig
from algoliasearch.http.base_transporter import BaseTransporter
from algoliasearch.http.exceptions import (
    AlgoliaUnreachableHostException,
    RequestException,
)
from algoliasearch.http.hosts import Host
from algoliasearch.http.request_options import RequestOptions
from algoliasearch.http.retry import RetryOutcome, RetryStrategy
from algoliasearch.http.verb import Verb


class Transporter(BaseTransporter):
    def __init__(self, config: BaseConfig) -> None:
        super().__init__(config)
        self._session: Optional[ClientSession] = None
        self._config = config
        self._retry_strategy = RetryStrategy()
        self._hosts: List[Host] = []

    async def close(self) -> None:
        if self._session is not None:
            _session = self._session
            self._session = None

            await _session.close()

    async def request(
        self,
        verb: Verb,
        path: str,
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

        path = self.build_path(path, query_parameters)

        for host in self._retry_strategy.valid_hosts(self._hosts):
            url = self.build_url(host, path)
            proxy = self.get_proxy(url)

            try:
                async with timeout(self._timeout / 1000):
                    resp = await self._session.request(
                        method=verb,
                        url=url,
                        headers=request_options.headers,
                        data=request_options.data,
                        proxy=proxy,
                    )

                    _raw_data = await resp.text()
                    response = ApiResponse(
                        verb=verb,
                        path=path,
                        url=url,
                        host=host.url,
                        status_code=resp.status,
                        headers=resp.headers,  # pyright: ignore # insensitive dict is still a dict
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

        raise AlgoliaUnreachableHostException(
            "Unreachable hosts. If the error persists, please visit our help center https://alg.li/support-unreachable-hosts or reach out to the Algolia Support team: https://alg.li/support"
        )


class EchoTransporter(Transporter):
    def __init__(self, config: BaseConfig) -> None:
        super().__init__(config)
        self._config = config
        self._retry_strategy = RetryStrategy()

    async def request(
        self,
        verb: Verb,
        path: str,
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
            query_parameters=request_options.query_parameters,
            headers=dict(request_options.headers),
            data=request_options.data,
            raw_data=request_options.data,  # type: ignore
        )
