import sys
import time

from typing import Optional, Union

from algoliasearch.exceptions import AlgoliaUnreachableHostException, \
    RequestException
from algoliasearch.http.hosts import Host, HostsCollection
from algoliasearch.http.request_options import RequestOptions
from algoliasearch.configs import Config
from algoliasearch.http.serializer import QueryParametersSerializer
from algoliasearch.http.verbs import Verbs

try:
    from algoliasearch.http.requester import Requester
except ImportError:  # Already imported.
    pass


class Transporter(object):
    def __init__(self, requester, config):
        # type: (Requester, Config) -> None

        self.__requester = requester
        self.__config = config
        self.__retry_strategy = RetryStrategy()

    def write(self, verb, path, data, request_options):
        # type: (str, str, Optional[Union[dict, list]], Optional[Union[dict, RequestOptions]]) -> dict # noqa: E501

        if request_options is None or isinstance(request_options, dict):
            request_options = RequestOptions.create(self.__config,
                                                    request_options)

        timeout = request_options.timeouts['writeTimeout']

        return self.__request(verb, self.__config.hosts['write'], path, data,
                              request_options, timeout)

    def read(self, verb, path, data, request_options):
        # type: (str, str, Optional[Union[dict, list]], Optional[Union[dict, RequestOptions]]) -> dict # noqa: E501

        if request_options is None or isinstance(request_options, dict):
            request_options = RequestOptions.create(self.__config,
                                                    request_options)

        timeout = request_options.timeouts['readTimeout']

        return self.__request(verb, self.__config.hosts['read'], path, data,
                              request_options, timeout)

    def __request(self, verb, hosts, path, data, request_options, timeout):
        # type: (str, HostsCollection, str, Optional[Union[dict, list]], RequestOptions, int) -> dict # noqa: E501

        hosts.reset()

        if isinstance(data, dict):
            data.update(request_options.data)

        query_parameters = dict(request_options.query_parameters)
        if verb == Verbs.GET:
            query_parameters.update(request_options.data)

        query_parameters_as_string = QueryParametersSerializer.serialize(
            query_parameters
        )

        for host in hosts:

            url = 'https://%s/%s?%s' % (
                host.url, path, query_parameters_as_string)

            response = self.__requester.request(verb.upper(), url,
                                                request_options.headers,
                                                data, timeout,
                                                self.__config.connect_timeout)

            decision = self.__retry_strategy.decide(host, response)

            if decision == RetryOutcome.SUCCESS:
                return response.content if response.content is not None else {}
            elif decision == RetryOutcome.FAIL:
                content = response.error_message
                if response.content and 'message' in response.content:
                    content = response.content['message']

                raise RequestException(content, response.status_code)

        raise AlgoliaUnreachableHostException('Unreachable hosts')


class Response(object):
    def __init__(self, status_code=None, content=None,
                 error_message='', is_timed_out_error=False,
                 is_network_error=False):
        # type: (int, Optional[dict], str, bool, bool) -> None

        self.status_code = status_code
        self.content = content
        self.error_message = error_message
        self.is_timed_out_error = is_timed_out_error
        self.is_network_error = is_network_error


class RetryStrategy(object):
    def decide(self, host, response):
        # type: (Host, Response) -> str

        host.last_use = time.time()

        if response.is_timed_out_error:
            host.retry_count += 1

            return RetryOutcome.RETRY
        elif self.__is_retryable(response):
            host.up = False
            return RetryOutcome.RETRY
        elif response.status_code is not None and self.__is_success(response):
            return RetryOutcome.SUCCESS

        return RetryOutcome.FAIL

    def __is_success(self, response):
        # type: (Response) -> bool

        return (response.status_code // 100) == 2

    def __is_retryable(self, response):
        # type: (Response) -> bool

        if response.is_network_error:
            return True

        return response.status_code is not None and (
                response.status_code // 100) != 2 and (
                       response.status_code // 100) != 4


class RetryOutcome(object):
    SUCCESS = 'SUCCESS'
    RETRY = 'RETRY'
    FAIL = 'FAIL'
