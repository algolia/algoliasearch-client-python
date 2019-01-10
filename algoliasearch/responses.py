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

        self.__raw_responses = raw_responses
        self.__index = index

    def get_task_ids(self):
        # type: () -> list

        task_ids = []
        for raw_response in self.__raw_responses:
            task_ids.append(raw_response['taskID'])

        return task_ids

    def wait(self):
        # type: () -> None

        for raw_response in self.__raw_responses:
            self.__index.wait_task(raw_response['taskID'])

    def __getitem__(self, key):
        # type:(int) -> dict

        return self.__raw_responses[key]

    def __len__(self):
        # type:() -> int

        return len(self.__raw_responses)


class MultipleResponse(Response):

    def __init__(self, responses):
        # type: (List[Response]) -> None

        self.responses = responses

    def wait(self):
        # type: () -> None

        for response in self.responses:
            response.wait()
