import abc

from typing import Optional, Union

from algoliasearch.http.request_options import RequestOptions
from algoliasearch.http.transporter import Transporter
from algoliasearch.http.verbs import Verbs


class Iterator(object):
    __metaclass__ = abc.ABCMeta

    def next(self):
        # type: () -> dict

        return self.__next__()

    def __iter__(self):
        # type: () -> Iterator

        return self

    @abc.abstractmethod
    def __next__(self):
        # type: () -> dict

        pass


class ObjectIterator(Iterator):

    def __init__(self, transporter, index_name, request_options=None):
        # type: (Transporter, str, Optional[Union[dict, RequestOptions]]) -> None  # noqa: E501

        self.__transporter = transporter
        self.__index_name = index_name
        self.__request_options = request_options
        self.__raw_response = None

    def __next__(self):
        # type: () -> dict

        data = {}

        if self.__raw_response:
            if len(self.__raw_response['hits']):
                return self.__raw_response['hits'].pop(0)

            if 'cursor' not in self.__raw_response:
                self.__raw_response = None
                raise StopIteration
            else:
                data['cursor'] = self.__raw_response['cursor']

        self.__raw_response = self.__transporter.read(
            Verbs.POST,
            '1/indexes/%s/browse' % self.__index_name,
            data,
            self.__request_options
        )

        return self.__next__()


class SynonymIterator(Iterator):

    def __init__(self, transporter, index_name, request_options=None):
        # type: (Transporter, str, Optional[Union[dict, RequestOptions]]) -> None  # noqa: E501

        self.__transporter = transporter
        self.__index_name = index_name
        self.__request_options = request_options
        self.__raw_response = None

        self.__data = {
            'hitsPerPage': 1000,
            'page': 0,
        }

    def __next__(self):
        # type: () -> dict

        if self.__raw_response:
            if len(self.__raw_response['hits']):
                hit = self.__raw_response['hits'].pop(0)

                hit.pop('_highlightResult')

                return hit

            if self.__raw_response['nbHits'] < self.__data['hitsPerPage']:
                self.__raw_response = None
                self.__data = {
                    'hitsPerPage': 1000,
                    'page': 0,
                }
                raise StopIteration

        self.__raw_response = self.__transporter.read(
            Verbs.POST,
            '1/indexes/%s/synonyms/search' % self.__index_name,
            self.__data,
            self.__request_options
        )

        self.__data['page'] += 1

        return self.__next__()
