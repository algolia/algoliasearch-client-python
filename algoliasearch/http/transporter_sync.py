from gzip import compress as gzip_compress
from json import dumps, loads
from sys import version_info
from typing import Iterator, Optional

from requests import Request, Session, Timeout

if version_info >= (3, 11):
    from typing import List, Self
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
from algoliasearch.http.sse import ServerSentEvent, iter_sse_events
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
        if (
            self._config.compression_type == "gzip"
            and isinstance(request_options.data, str)
            and len(request_options.data) >= self._config.compression_threshold
        ):
            request_options.data = gzip_compress(request_options.data.encode("utf-8"))
            request_options.headers["content-encoding"] = "gzip"

        for host in self._retry_strategy.valid_hosts(self._hosts):
            url = self.build_url(host, path)
            proxies = self.get_proxies(url)

            req = self._session.prepare_request(
                Request(
                    method=verb,
                    url=url,
                    headers=request_options.headers,
                    data=request_options.data,
                )
            )

            try:
                connect_timeout = (
                    request_options.timeouts["connect"] * (host.retry_count + 1)
                ) / 1000
                read_timeout = self._timeout / 1000

                resp = self._session.send(
                    req,
                    timeout=(connect_timeout, read_timeout),
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

    def request_stream(
        self,
        verb: Verb,
        path: str,
        request_options: RequestOptions,
        use_read_transporter: bool,
    ) -> Iterator[ServerSentEvent]:
        if self._session is None:
            self._session = Session()
            self._session.mount("https://", HTTPAdapter(max_retries=Retry(connect=0)))

        request_options.headers["accept"] = "text/event-stream"

        query_parameters = self.prepare(
            request_options, verb == Verb.GET or use_read_transporter
        )

        path = self.build_path(path, query_parameters)

        valid_hosts = self._retry_strategy.valid_hosts(self._hosts)
        if not valid_hosts:
            raise AlgoliaUnreachableHostException(
                "No hosts available for streaming request"
            )
        host = valid_hosts[0]
        url = self.build_url(host, path)
        proxies = self.get_proxies(url)

        req = self._session.prepare_request(
            Request(
                method=verb,
                url=url,
                headers=request_options.headers,
                data=request_options.data,
            )
        )

        connect_timeout = request_options.timeouts["connect"] / 1000
        read_timeout = self._timeout / 1000

        resp = self._session.send(
            req,
            timeout=(connect_timeout, read_timeout),
            proxies=proxies,
            stream=True,
        )

        try:
            if resp.status_code >= 400:
                error_text = resp.text
                raise RequestException(error_text, resp.status_code)

            for event in iter_sse_events(resp.iter_content(chunk_size=None)):
                yield event
        finally:
            resp.close()


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
        if (
            self._config.compression_type == "gzip"
            and isinstance(request_options.data, str)
            and len(request_options.data) >= self._config.compression_threshold
        ):
            request_options.data = gzip_compress(request_options.data.encode("utf-8"))
            request_options.headers["content-encoding"] = "gzip"

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

    def request_stream(
        self,
        verb: Verb,
        path: str,
        request_options: RequestOptions,
        use_read_transporter: bool,
    ) -> Iterator[ServerSentEvent]:
        self.prepare(request_options, verb == Verb.GET or use_read_transporter)

        data = dumps(
            {
                "verb": verb,
                "path": path,
                "status_code": 200,
                "host": self._retry_strategy.valid_hosts(self._hosts)[0].url,
                "timeouts": {
                    "connect": request_options.timeouts["connect"],
                    "response": self._timeout,
                },
                "query_parameters": request_options.query_parameters,
                "headers": dict(request_options.headers),
                "data": request_options.data,
            }
        )

        yield ServerSentEvent(data=data, event="", id=None, retry=None)
