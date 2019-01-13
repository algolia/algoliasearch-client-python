import unittest

import mock

from algoliasearch.http.request_options import RequestOptions
from algoliasearch.search_index import SearchIndex
from algoliasearch.configs import SearchConfig
from algoliasearch.http.transporter import Transporter
from algoliasearch.http.requester import Requester


class TestSearchIndex(unittest.TestCase):
    def setUp(self):
        self.config = SearchConfig('foo', 'bar')
        requester = Requester()
        self.transporter = Transporter(requester, self.config)
        self.transporter.read = mock.Mock(name="read")
        self.transporter.read.return_value = {}
        self.transporter.write = mock.Mock(name="write")
        self.transporter.write.return_value = {}
        self.index = SearchIndex(self.transporter, self.config, 'foo')

    def test_app_id_getter(self):
        self.assertEqual(self.index.app_id, 'foo')

    def test_get_objects_with_request_options_as_none(self):
        self.index.get_objects([1])
        self.transporter.read.assert_called_once_with(
            'POST',
            '1/indexes/*/objects',
            {'requests': [{'indexName': 'foo', 'objectID': '1'}]}
        )

    def test_get_objects_with_request_options_as_dict(self):
        self.index.get_objects([1], {})
        self.transporter.read.assert_called_once_with(
            'POST',
            '1/indexes/*/objects',
            {'requests': [{'indexName': 'foo', 'objectID': '1'}]}
        )

    def test_get_objects_with_request_options_as_request_options(self):
        request_options = RequestOptions.create(self.config, {})
        self.index.get_objects([1], request_options)
        request_options.data['requests'] = [
            {'indexName': 'foo', 'objectID': '1'}]
        self.transporter.read.assert_called_once_with(
            'POST',
            '1/indexes/*/objects',
            request_options
        )
