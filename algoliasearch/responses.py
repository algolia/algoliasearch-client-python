import time

import abc

from typing import List, Union, Optional

from algoliasearch.exceptions import RequestException
from algoliasearch.helpers import get_items, sleep_for, endpoint
from algoliasearch.http.request_options import RequestOptions
from algoliasearch.http.verb import Verb
from algoliasearch.http.hosts import CallType

try:
    from algoliasearch.search_index import SearchIndex
except ImportError:  # Already imported.
    pass

try:
    from algoliasearch.search_client import SearchClient
except ImportError:  # Already imported.
    pass


class Response(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def wait(self, request_options=None):
        # type: (Optional[Union[RequestOptions, dict]]) -> Response

        pass  # pragma: no cover


class IndexingResponse(Response):
    def __init__(self, index, raw_responses):
        # type: (SearchIndex, List[dict]) -> None

        self._index = index
        self.raw_responses = raw_responses
        self.waited = False

    def wait(self, request_options=None):
        # type: (Optional[Union[RequestOptions, dict]]) -> IndexingResponse

        if not self.waited:
            for raw_response in self.raw_responses:
                self._index._sync().wait_task(raw_response["taskID"], request_options)

        # No longer waits on this responses.
        self.waited = True

        return self

    def __getitem__(self, key):
        # type:(int) -> dict

        return self.raw_responses[key]


class MultipleResponse(Response):
    def __init__(self, responses=None):
        # type: (List[Response]) -> None

        self.responses = [] if responses is None else responses
        self._waitable = list(self.responses)

    def push(self, response):
        # type: (Response) -> None

        self.responses.append(response)

        self._waitable.append(response)

    def wait(self, request_options=None):
        # type: (Optional[Union[RequestOptions, dict]])-> MultipleResponse

        for response in self._waitable:
            response.wait(request_options)

        # No longer waits on this responses.
        self._waitable = []

        return self

    def __getitem__(self, key):
        # type:(int) -> Response

        return self.responses[key]


class AddApiKeyResponse(Response):
    def __init__(self, client, raw_response):
        # type: (SearchClient, dict) -> None

        self.raw_response = raw_response
        self._client = client
        self._done = False

    def wait(self, request_options=None):
        # type: (Optional[Union[RequestOptions, dict]]) -> AddApiKeyResponse

        retries_count = 1

        while not self._done:
            try:
                self._client._sync().get_api_key(
                    self.raw_response["key"], request_options
                )
                self._done = True
            except RequestException as e:
                if e.status_code != 404:
                    raise e
                retries_count += 1
                sleep_for(
                    retries_count, self._client._config.wait_task_time_before_retry
                )

        return self

    def __getitem__(self, key):
        # type:(str) -> Union[int, str, dict, list]

        return self.raw_response[key]


class UpdateApiKeyResponse(Response):
    def __init__(self, client, raw_response, request_options):
        # type: (SearchClient, dict, RequestOptions) -> None

        self.raw_response = raw_response
        self._client = client
        self._request_options = request_options
        self._done = False

    def wait(self, request_options=None):
        # type: (Optional[Union[RequestOptions, dict]]) -> UpdateApiKeyResponse

        retries_count = 1

        while not self._done:
            api_key = self._client._sync().get_api_key(
                self.raw_response["key"], request_options
            )

            self._done = self._have_changed(api_key)

            if not self._done:
                retries_count += 1
                sleep_for(
                    retries_count, self._client._config.wait_task_time_before_retry
                )

        return self

    def _have_changed(self, api_key):
        # type: (dict) -> bool

        valid_keys = (
            "acl",
            "indexes",
            "referers",
            "restrictSources",
            "queryParameters",
            "description",
            "maxQueriesPerIPPerHour",
            "maxHitsPerQuery",
        )

        body = self._request_options.data

        valid_key_exists = any([key in valid_keys for key in body.keys()])

        return not valid_key_exists or any(
            [
                (valid_key in body and body[valid_key] == api_key.get(valid_key))
                for valid_key in valid_keys
            ]
        )

    def __getitem__(self, key):
        # type:(str) -> Union[int, str, dict, list]

        return self.raw_response[key]


class DeleteApiKeyResponse(Response):
    def __init__(self, client, raw_response, key):
        # type: (SearchClient, dict, str) -> None

        self.raw_response = raw_response
        self._client = client
        self._key = key
        self._done = False

    def wait(self, request_options=None):
        # type: (Optional[Union[RequestOptions, dict]]) -> DeleteApiKeyResponse

        retries_count = 1

        while not self._done:
            try:
                self._client._sync().get_api_key(self._key, request_options)
            except RequestException as e:
                self._done = e.status_code == 404

            if not self._done:
                retries_count += 1
                sleep_for(
                    retries_count, self._client._config.wait_task_time_before_retry
                )

        return self

    def __getitem__(self, key):
        # type:(str) -> Union[int, str, dict, list]

        return self.raw_response[key]


class RestoreApiKeyResponse(Response):
    def __init__(self, client, raw_response, key):
        # type: (SearchClient, dict, str) -> None

        self.raw_response = raw_response
        self._client = client
        self._key = key
        self._done = False

    def wait(self, request_options=None):
        # type: (Optional[Union[RequestOptions, dict]]) -> RestoreApiKeyResponse # noqa: E501

        retries_count = 1

        while not self._done:
            try:
                self._client._sync().get_api_key(self._key, request_options)
                self._done = True
            except RequestException as e:
                if e.status_code != 404:
                    raise e
                retries_count += 1
                sleep_for(
                    retries_count, self._client._config.wait_task_time_before_retry
                )

        return self

    def __getitem__(self, key):
        # type:(str) -> Union[int, str, dict, list]

        return self.raw_response[key]


class MultipleIndexBatchIndexingResponse(Response):
    def __init__(self, client, raw_response):
        # type: (SearchClient, dict) -> None

        self.raw_response = raw_response
        self._client = client
        self._done = False

    def wait(self, request_options=None):
        # type: (Optional[Union[RequestOptions, dict]]) -> MultipleIndexBatchIndexingResponse # noqa: E501

        while not self._done:
            for index_name, task_id in get_items(self.raw_response["taskID"]):
                self._client._sync().wait_task(index_name, task_id, request_options)
            self._done = True

        return self

    def __getitem__(self, key):
        # type:(str) -> Union[int, str, dict, list]

        return self.raw_response[key]


class DictionaryResponse(Response):
    def __init__(self, client, raw_response):
        # type: (SearchClient, dict) -> None

        self.raw_response = raw_response
        self._client = client
        self._done = False

    def wait(self, request_options=None):
        # type: (Optional[Union[RequestOptions, dict]]) -> DictionaryResponse # noqa: E501

        while not self._done:
            res = self._client.custom_request(
                {},
                endpoint("1/task/{}", self.raw_response["taskID"]),
                Verb.GET,
                CallType.READ,
            )

            if res is not None and res.get("status") == "published":
                self._done = True

            time.sleep(self._client._config.wait_task_time_before_retry / 1000000.0)

        return self

    def __getitem__(self, key):
        # type:(str) -> Union[int, str, dict, list]

        return self.raw_response[key]
