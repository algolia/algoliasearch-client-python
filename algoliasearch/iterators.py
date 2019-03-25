import abc

from typing import Optional, Union

from algoliasearch.http.request_options import RequestOptions
from algoliasearch.http.transporter import Transporter
from algoliasearch.http.verb import Verb


class Iterator(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, transporter, index_name, request_options=None):
        # type: (Transporter, str, Optional[Union[dict, RequestOptions]]) -> None  # noqa: E501

        self._transporter = transporter
        self._index_name = index_name
        self._request_options = request_options
        self._raw_response = {}  # type: dict

    def next(self):
        # type: () -> dict

        return self.__next__()  # pragma: no cover

    def __next__(self):
        # type: () -> dict

        pass  # pragma: no cover

    def __iter__(self):
        # type: () -> Iterator

        return self


class PaginatorIterator(Iterator):
    def __init__(self, transporter, index_name, request_options=None):
        # type: (Transporter, str, Optional[Union[dict, RequestOptions]]) -> None  # noqa: E501

        super(PaginatorIterator, self).__init__(transporter, index_name,
                                                request_options)
        self._data = {
            'hitsPerPage': 1000,
            'page': 0,
        }

    def __next__(self):
        # type: () -> dict

        if self._raw_response:
            if len(self._raw_response['hits']):
                hit = self._raw_response['hits'].pop(0)

                hit.pop('_highlightResult')

                return hit

            if self._raw_response['nbHits'] < self._data['hitsPerPage']:
                self._raw_response = {}
                self._data = {
                    'hitsPerPage': 1000,
                    'page': 0,
                }
                raise StopIteration

        self._raw_response = self._transporter.read(
            Verb.POST,
            self.get_endpoint(),
            self._data,
            self._request_options
        )

        self._data['page'] += 1

        return self.__next__()

    @abc.abstractmethod
    def get_endpoint(self):
        # type: () -> str

        pass  # pragma: no cover


class ObjectIterator(Iterator):

    def __next__(self):
        # type: () -> dict

        data = {}  # type: dict

        if self._raw_response:
            if len(self._raw_response['hits']):
                return self._raw_response['hits'].pop(0)

            if 'cursor' not in self._raw_response:
                self._raw_response = {}
                raise StopIteration
            else:
                data['cursor'] = self._raw_response['cursor']

        self._raw_response = self._transporter.read(
            Verb.POST,
            '1/indexes/{}/browse'.format(self._index_name),
            data,
            self._request_options
        )

        return self.__next__()


class SynonymIterator(PaginatorIterator):

    def get_endpoint(self):
        # type: () -> str

        return '1/indexes/{}/synonyms/search'.format(self._index_name)


class RuleIterator(PaginatorIterator):

    def get_endpoint(self):
        # type: () -> str

        return '1/indexes/{}/rules/search'.format(self._index_name)
