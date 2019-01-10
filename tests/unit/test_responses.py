import unittest

from algoliasearch.responses import IndexingResponse
from algoliasearch.search_client import SearchClient
from algoliasearch.search_index import SearchIndex


class TestIndexingResponse(unittest.TestCase):
    def test_dict_access(self):
        response = {
            'foo': 'bar',
        }

        index = SearchClient.create('foo', 'bar').init_index('foo')
        response = FooResponse(index, response)
        self.assertEqual(response['foo'], 'bar')


class FooResponse(IndexingResponse):
    def wait(self):
        pass
