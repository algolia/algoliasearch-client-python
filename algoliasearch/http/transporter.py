import time

from typing import Optional, Union, Dict, Any, List
from algoliasearch.exceptions import AlgoliaUnreachableHostException, RequestException
from algoliasearch.http.hosts import Host
from algoliasearch.http.request_options import RequestOptions
from algoliasearch.configs import Config
from algoliasearch.http.serializer import QueryParametersSerializer, DataSerializer
from algoliasearch.http.verb import Verb

try:
    from algoliasearch.http.requester import Requester
except ImportError:  # Already imported.
    pass


class Transporter(object):
    def __init__(self, requester, config):
        # type: (Requester, Config) -> None

        self._requester = requester
        self._config = config
        self._retry_strategy = RetryStrategy()

    def write(self, verb, path, data, request_options):
        # type: (str, str, Optional[Union[dict, list]], Optional[Union[dict, RequestOptions]]) -> dict # noqa: E501

        if request_options is None or isinstance(request_options, dict):
            request_options = RequestOptions.create(self._config, request_options)

        timeout = request_options.timeouts["writeTimeout"]

        hosts = self._config.hosts.write()

        return self.request(verb, hosts, path, data, request_options, timeout)

    def read(self, verb, path, data, request_options):
        # type: (str, str, Optional[Union[dict, list]], Optional[Union[dict, RequestOptions]]) -> dict # noqa: E501

        if request_options is None or isinstance(request_options, dict):
            request_options = RequestOptions.create(self._config, request_options)

        timeout = request_options.timeouts["readTimeout"]

        hosts = self._config.hosts.read()

        return self.request(verb, hosts, path, data, request_options, timeout)

    def request(self, verb, hosts, path, data, request_options, timeout):
        # type: (str, List[Host], str, Optional[Union[dict, list]], RequestOptions, int) -> dict # noqa: E501

        if isinstance(data, dict):
            data.update(request_options.data)

        query_parameters = dict(request_options.query_parameters)
        if verb == Verb.GET:
            query_parameters.update(request_options.data)

        relative_url = "{}?{}".format(
            path, QueryParametersSerializer.serialize(query_parameters)
        )

        request = Request(
            verb.upper(),
            request_options.headers,
            data,
            self._config.connect_timeout,
            timeout,
            self._config.proxies,
        )

        return self.retry(hosts, request, relative_url)

    def retry(self, hosts, request, relative_url):
        # type: (List[Host], Request, str) -> dict

        for host in self._retry_strategy.valid_hosts(hosts):

            request.url = "https://{}/{}".format(host.url, relative_url)

            response = self._requester.send(request)

            decision = self._retry_strategy.decide(host, response)

            if decision == RetryOutcome.SUCCESS:
                return response.content if response.content is not None else {}
            elif decision == RetryOutcome.FAIL:
                content = response.error_message
                if response.content and "message" in response.content:
                    content = response.content["message"]

                raise RequestException(content, response.status_code)

        raise AlgoliaUnreachableHostException("Unreachable hosts")

    def close(self):
        # type: () -> None

        self._requester.close()


class Request(object):
    def __init__(
        self, verb, headers, data, connect_timeout, timeout, proxies={}
    ):  # noqa: E501
        # type: (str, dict, Optional[Union[dict, list]], int, int, dict) -> None  # noqa: E501

        self.verb = verb
        self.data = data
        self.data_as_string = "" if data is None else DataSerializer.serialize(data)
        self.headers = headers
        self.connect_timeout = connect_timeout
        self.timeout = timeout
        self.proxies = proxies
        self.url = ""

    def __str__(self):
        return "Request({}, {}, {}, {}, {}, {}, {})".format(
            self.verb,
            self.url,
            self.headers,
            self.data_as_string,
            self.connect_timeout,
            self.timeout,
            self.proxies,
        )

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        # type: (object) -> bool

        return self.__dict__ == other.__dict__


class Response(object):
    def __init__(
        self,
        status_code=None,
        content=None,
        error_message="",
        is_timed_out_error=False,
        is_network_error=False,
    ):
        # type: (int, Optional[Dict[str, Any]], str, bool, bool) -> None

        self.status_code = status_code
        self.content = content
        self.error_message = error_message
        self.is_timed_out_error = is_timed_out_error
        self.is_network_error = is_network_error


class RetryStrategy(object):
    def valid_hosts(self, hosts):
        # type: (list) -> list

        for host in hosts:
            if not host.up and self._now() - host.last_use > Host.TTL:
                host.up = True

        return [host for host in hosts if host.up]

    def _now(self):
        # type: () -> float

        return time.time()

    def decide(self, host, response):
        # type: (Host, Response) -> str

        host.last_use = time.time()

        if response.is_timed_out_error:
            host.retry_count += 1

            return RetryOutcome.RETRY
        elif self._is_retryable(response):
            host.up = False

            return RetryOutcome.RETRY
        elif response.status_code is not None and self._is_success(response):

            return RetryOutcome.SUCCESS

        return RetryOutcome.FAIL

    def _is_success(self, response):
        # type: (Response) -> bool

        return response.status_code is not None and (response.status_code // 100) == 2

    def _is_retryable(self, response):
        # type: (Response) -> bool

        if response.is_network_error:
            return True

        return (
            response.status_code is not None
            and (response.status_code // 100) != 2
            and (response.status_code // 100) != 4
        )


class RetryOutcome(object):
    SUCCESS = "SUCCESS"
    RETRY = "RETRY"
    FAIL = "FAIL"
