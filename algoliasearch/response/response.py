import abc

from typing import Any


# @todo Resolve `from algoliasearch.search_index import SearchIndex`

class Response(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, index, response=None):
        # type: (SearchIndex, dict) -> None

        self._index = index
        self.body = {} if response is None else response

    @abc.abstractmethod
    def wait(self):
        # type:() -> None

        pass

    def __getitem__(self, key):
        # type:(Any) -> Any

        return self.body[key]

    def __setitem__(self, key, value):
        # type:(Any, Any) -> None

        self.body[key] = value

    def __delitem__(self, key):
        # type:(Any) -> None

        del self.body[key]

    def __contains__(self, key):
        # type:(Any) -> bool

        return key in self.body

    def __len__(self):
        # type:() -> int

        return len(self.body)

    def __repr__(self):
        # type:() -> str

        return repr(self.body)
