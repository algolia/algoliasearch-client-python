from json import loads
from sys import version_info

from requests import Request, Session, Timeout

if version_info >= (3, 11):
    from typing import List, Optional, Self
else:
    from typing_extensions import List, Self

from requests.adapters import HTTPAdapter
from urllib3.util import Retry

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


class TransporterSync(BaseTransporter):
    def __init__(self, config: BaseConfig) -> None:
        super().__init__(config)
        self._session: Optional[Session] = None
        self._config = config
        self._retry_strategy = RetryStrategy()
        self._hosts: List[Host] = []

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        pass

    def close(self) -> None:
        if self._session is not None:
            _session = self._session
            self._session = None

            _session.close()

    def request(
        self,
        verb: Verb,
        path: str,
        request_options: RequestOptions,
        use_read_transporter: bool,
    ) -> ApiResponse:
        if self._session is None:
            self._session = Session()
            self._session.mount("https://", HTTPAdapter(max_retries=Retry(connect=0)))

        query_parameters = self.prepare(
            request_options, verb == Verb.GET or use_read_transporter
        )

        path = self.build_path(path, query_parameters)

        for host in self._retry_strategy.valid_hosts(self._hosts):
            url = self.build_url(host, path)
            proxies = self.get_proxies(url)

            req = Request(
                method=verb,
                url=url,
                headers=request_options.headers,
                data=request_options.data,
            ).prepare()

            try:
                resp = self._session.send(
                    req,
                    timeout=self._timeout / 1000,
                    proxies=proxies,
                )

                response = ApiResponse(
                    verb=verb,
                    path=path,
                    url=url,
                    host=host.url,
                    status_code=resp.status_code,
                    headers=resp.headers,  # type: ignore # insensitive dict is still a dict
                    data=resp.text,
                    raw_data=resp.text,
                    error_message=str(resp.reason),
                )
            except Timeout as e:
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


class EchoTransporterSync(TransporterSync):
    def __init__(self, config: BaseConfig) -> None:
        super().__init__(config)
        self._config = config
        self._retry_strategy = RetryStrategy()

    def request(
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
