import abc

from typing import List

from algoliasearch.exceptions import RequestException
from algoliasearch.helpers import get_items
from algoliasearch.http.request_options import RequestOptions

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
    def wait(self):
        # type:() -> Response

        pass  # pragma: no cover


class IndexingResponse(Response):

    def __init__(self, index, raw_responses):
        # type: (SearchIndex, List[dict]) -> None

        self._index = index
        self.raw_responses = raw_responses
        self.waited = False

    def wait(self):
        # type: () -> IndexingResponse

        if not self.waited:
            for raw_response in self.raw_responses:
                self._index._sync().wait_task(raw_response['taskID'])

        # No longer waits on this responses.
        self.waited = True

        return self


class MultipleResponse(Response):

    def __init__(self, responses=None):
        # type: (List[Response]) -> None

        self.responses = [] if responses is None else responses
        self._waitable = list(self.responses)

    def push(self, response):
        # type: (Response) -> None

        self.responses.append(response)

        self._waitable.append(response)

    def wait(self):
        # type: () -> MultipleResponse

        for response in self._waitable:
            response.wait()

        # No longer waits on this responses.
        self._waitable = []

        return self


class AddApiKeyResponse(Response):

    def __init__(self, client, raw_response):
        # type: (SearchClient, dict) -> None

        self.raw_response = raw_response
        self._client = client
        self._done = False

    def wait(self):
        # type: () -> AddApiKeyResponse

        while not self._done:
            try:
                self._client._sync().get_api_key(self.raw_response['key'])
                self._done = True
            except RequestException as e:
                if e.status_code != 404:
                    raise e

        return self


class UpdateApiKeyResponse(Response):

    def __init__(self, client, raw_response, request_options):
        # type: (SearchClient, dict, RequestOptions) -> None

        self.raw_response = raw_response
        self._client = client
        self._request_options = request_options
        self._done = False

    def wait(self):
        # type: () -> UpdateApiKeyResponse

        while not self._done:
            api_key = self._client._sync().get_api_key(
                self.raw_response['key']
            )

            if self._have_changed(api_key):
                break

        return self

    def _have_changed(self, api_key):
        # type: (dict) -> bool

        valid_keys = (
            'acl', 'indexes', 'referers',
            'restrictSources', 'queryParameters', 'description',
            'validity', 'maxQueriesPerIPPerHour', 'maxHitsPerQuery',
        )

        body = self._request_options.data

        return any([(valid_key in body and body[valid_key] == api_key.get(
            valid_key)) for valid_key in valid_keys])


class DeleteApiKeyResponse(Response):

    def __init__(self, client, raw_response, key):
        # type: (SearchClient, dict, str) -> None

        self.raw_response = raw_response
        self._client = client
        self._key = key
        self._done = False

    def wait(self):
        # type: () -> DeleteApiKeyResponse

        while not self._done:
            try:
                self._client._sync().get_api_key(self._key)
            except RequestException as e:
                self._done = e.status_code == 404

        return self


class RestoreApiKeyResponse(Response):

    def __init__(self, client, raw_response, key):
        # type: (SearchClient, dict, str) -> None

        self.raw_response = raw_response
        self._client = client
        self._key = key
        self._done = False

    def wait(self):
        # type: () -> RestoreApiKeyResponse

        while not self._done:
            try:
                self._client._sync().get_api_key(self._key)
                self._done = True
            except RequestException as e:
                if e.status_code != 404:
                    raise e

        return self


class MultipleIndexBatchIndexingResponse(Response):

    def __init__(self, client, raw_response):
        # type: (SearchClient, dict) -> None

        self.raw_response = raw_response
        self._client = client
        self._done = False

    def wait(self):
        # type: () -> MultipleIndexBatchIndexingResponse

        while not self._done:
            for index_name, task_id in get_items(self.raw_response['taskID']):
                self._client._sync().wait_task(index_name, task_id)
            self._done = True

        return self
