import abc

from typing import List

from algoliasearch.exceptions import RequestException

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
                print(e.status_code)
                if e.status_code is not 404:
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
