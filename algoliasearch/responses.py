import abc

from typing import List, Any

try:
    from algoliasearch.search_index import SearchIndex
except ImportError:  # Already imported.
    pass


class Response(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def wait(self):
        # type:() -> None

        pass


class IndexingResponse(Response):

    def __init__(self, index, raw_responses):
        # type: (SearchIndex, List[dict]) -> None

        self.__index = index

        self.raw_responses = raw_responses
        self.__raw_waitable_responses = list(raw_responses)

    def wait(self):
        # type: () -> None

        for raw_response in self.__raw_waitable_responses:
            self.__index.wait_task(raw_response['taskID'])

        # No longer waits on this responses.
        self.__raw_waitable_responses = []


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
        # type: () -> None

        for response in self.__waitable:
            response.wait()

        # No longer waits on this responses.
        self.__waitable = []


class NullResponse(Response):

    def wait(self):
        # type: () -> None

        pass
