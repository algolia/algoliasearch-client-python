from typing import Optional, Union

from algoliasearch.http.request_options import RequestOptions
from algoliasearch.http.transporter import Transporter
from algoliasearch.http.verbs import Verbs


class ObjectIterator(object):
    def __init__(self, transporter, index_name, request_options=None):
        # type: (Transporter, str, Optional[Union[dict, RequestOptions]]) -> None  # noqa: E501

        self.__transporter = transporter
        self.__index_name = index_name
        self.__request_options = request_options
        self.__raw_response = None

    def next(self):
        return self.__next__()

    def __iter__(self):
        return self

    def __next__(self):
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
