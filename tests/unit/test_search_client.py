import unittest

from algoliasearch.search_client import SearchClient
from algoliasearch.search_index import SearchIndex
from algoliasearch.configs import SearchConfig
from algoliasearch.http.transporter import Transporter
from algoliasearch.http.requester import Requester


class TestSearchClient(unittest.TestCase):
    def test_create(self):
        client = SearchClient.create('foo', 'bar')

        self.assertIsInstance(client, SearchClient)

    def test_init_index(self):
        index = SearchClient.create('foo', 'bar').init_index('foo')

        self.assertIsInstance(index, SearchIndex)

    def test_app_id_getter(self):
        client = SearchClient.create('foo', 'bar')

        self.assertEqual(client.app_id, 'foo')
