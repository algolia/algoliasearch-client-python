import abc
import asyncio

from typing import Optional, Union

from algoliasearch.http.request_options import RequestOptions
from algoliasearch.http.transporter import Transporter
from algoliasearch.http.verb import Verb
from algoliasearch.iterators import Iterator


class PaginatorIteratorAsync(Iterator):
    def __init__(self, transporter, index_name, request_options=None):
        # type: (Transporter, str, Optional[Union[dict, RequestOptions]]) -> None  # noqa: E501

        super(PaginatorIteratorAsync, self).__init__(
            transporter, index_name, request_options
        )
        self._data = {
            "hitsPerPage": 1000,
            "page": 0,
        }

    def __aiter__(self):
        # type: () -> PaginatorIteratorAsync

        return self  # pragma: no cover

    @asyncio.coroutine
    def __anext__(self):  # type: ignore
        # type: () -> dict

        if self._raw_response:
            if len(self._raw_response["hits"]):
                hit = self._raw_response["hits"].pop(0)

                hit.pop("_highlightResult")

                return hit

            if self._raw_response["nbHits"] < self._data["hitsPerPage"]:
                self._raw_response = {}
                self._data = {
                    "hitsPerPage": 1000,
                    "page": 0,
                }
                raise StopAsyncIteration

        self._raw_response = yield from self._transporter.read(
            Verb.POST, self.get_endpoint(), self._data, self._request_options
        )

        self._data["page"] += 1

        return self.__anext__()

    @abc.abstractmethod
    def get_endpoint(self):
        # type: () -> str

        pass  # pragma: no cover


class ObjectIteratorAsync(Iterator):
    def __aiter__(self):
        # type: () -> ObjectIteratorAsync

        return self  # pragma: no cover

    @asyncio.coroutine
    def __anext__(self):  # type: ignore
        # type: () -> dict

        data = {}  # type: dict

        if self._raw_response:
            if len(self._raw_response["hits"]):
                result = self._raw_response["hits"].pop(0)

                return result

            if "cursor" not in self._raw_response:
                self._raw_response = {}
                raise StopAsyncIteration
            else:
                data["cursor"] = self._raw_response["cursor"]

        self._raw_response = yield from self._transporter.read(
            Verb.POST,
            "1/indexes/{}/browse".format(self._index_name),
            data,
            self._request_options,
        )

        return (yield from self.__anext__())


class SynonymIteratorAsync(PaginatorIteratorAsync):
    def get_endpoint(self):
        # type: () -> str

        return "1/indexes/{}/synonyms/search".format(self._index_name)


class RuleIteratorAsync(PaginatorIteratorAsync):
    def get_endpoint(self):
        # type: () -> str

        return "1/indexes/{}/rules/search".format(self._index_name)
