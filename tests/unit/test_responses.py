import unittest

from algoliasearch.responses import IndexingResponse
from algoliasearch.search_client import SearchClient


class TestIndexingResponse(unittest.TestCase):
    def test_dict_access(self):
        response = {
            'foo': 'bar',
        }

        index = SearchClient.create('foo', 'bar').init_index('foo')
        response = FooResponse(index, [response])
        self.assertEqual(response.raw_responses[0]['foo'], 'bar')


class FooResponse(IndexingResponse):
    def wait(self):
        pass
