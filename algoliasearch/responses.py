import abc

from typing import List

from algoliasearch.exceptions import RequestException
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

        pass


class IndexingResponse(Response):

    def __init__(self, index, raw_responses):
        # type: (SearchIndex, List[dict]) -> None

        self.__index = index

        self.raw_responses = raw_responses
        self.__raw_waitable_responses = list(raw_responses)

    def wait(self):
        # type: () -> IndexingResponse

        for raw_response in self.__raw_waitable_responses:
            self.__index.wait_task(raw_response['taskID'])

        # No longer waits on this responses.
        self.__raw_waitable_responses = []

        return self


class MultipleResponse(Response):

    def __init__(self, responses=None):
        # type: (List[Response]) -> None

        self.responses = [] if responses is None else responses
        self.__waitable = list(self.responses)

    def push(self, response):
        # type: (Response) -> None

        self.responses.append(response)

        self.__waitable.append(response)

    def wait(self):
        # type: () -> MultipleResponse

        for response in self.__waitable:
            response.wait()

        # No longer waits on this responses.
        self.__waitable = []

        return self


class NullResponse(Response):

    def wait(self):
        # type: () -> NullResponse

        return self


class AssignUserIdResponse(Response):

    def __init__(self, client, user_id):
        # type: (SearchClient, str) -> None

        self.__client = client
        self.__user_id = user_id
        self.__done = False

    def wait(self):
        # type: () -> AssignUserIdResponse

        while not self.__done:
            try:
                self.__client.get_user_id(self.__user_id)
                self.__done = True
            except RequestException as e:
                if e.status_code != 404:
                    raise e

        return self


class RemoveUserIdResponse(Response):

    def __init__(self, client, user_id):
        # type: (SearchClient, str) -> None

        self.__client = client
        self.__user_id = user_id
        self.__done = False

    def wait(self):
        # type: () -> RemoveUserIdResponse

        while not self.__done:
            try:
                self.__client.get_user_id(self.__user_id)
            except RequestException as e:
                self.__done = e.status_code == 404

        return self


class AddApiKeyResponse(Response):

    def __init__(self, client, raw_response):
        # type: (SearchClient, dict) -> None

        self.raw_response = raw_response
        self.__client = client
        self.__done = False

    def wait(self):
        # type: () -> AddApiKeyResponse

        while not self.__done:
            try:
                self.__client.get_api_key(self.raw_response['key'])
                self.__done = True
            except RequestException as e:
                if e.status_code != 404:
                    raise e

        return self


class UpdateApiKeyResponse(Response):

    def __init__(self, client, raw_response, request_options):
        # type: (SearchClient, dict, RequestOptions) -> None

        self.raw_response = raw_response
        self.__client = client
        self.__request_options = request_options
        self.__done = False

    def wait(self):
        # type: () -> UpdateApiKeyResponse

        while not self.__done:
            api_key = self.__client.get_api_key(self.raw_response['key'])

            if self.__have_changed(api_key):
                break

        return self

    def __have_changed(self, api_key):
        # type: (dict) -> bool

        valid_keys = [
            'acl', 'indexes', 'referers',
            'restrictSources', 'queryParameters', 'description',
            'validity', 'maxQueriesPerIPPerHour', 'maxHitsPerQuery',
        ]

        for valid_key in valid_keys:
            if valid_key in self.__request_options.data:
                updated_value = self.__request_options.data[valid_key]
                if updated_value == api_key.get(valid_key):
                    return True

        return False


class DeleteApiKeyResponse(Response):

    def __init__(self, client, raw_response, key):
        # type: (SearchClient, dict, str) -> None

        self.raw_response = raw_response
        self.__client = client
        self.__key = key
        self.__done = False

    def wait(self):
        # type: () -> DeleteApiKeyResponse

        while not self.__done:
            try:
                self.__client.get_api_key(self.__key)
            except RequestException as e:
                self.__done = e.status_code == 404

        return self


class RestoreApiKeyResponse(Response):

    def __init__(self, client, raw_response, key):
        # type: (SearchClient, dict, str) -> None

        self.raw_response = raw_response
        self.__client = client
        self.__key = key
        self.__done = False

    def wait(self):
        # type: () -> RestoreApiKeyResponse

        while not self.__done:
            try:
                self.__client.get_api_key(self.__key)
                self.__done = True
            except RequestException as e:
                if e.status_code != 404:
                    raise e

        return self
