import unittest

from algoliasearch.search_client import SearchClient
from algoliasearch.search_index import SearchIndex
from algoliasearch.configs.search_config import SearchConfig
from algoliasearch.http.transporter import Transporter
from algoliasearch.http.requester import Requester


class TestSearchClient(unittest.TestCase):
    def test_init(self):
        config = SearchConfig('foo', 'bar')
        requester = Requester()
        transporter = Transporter(requester, config)
        client = SearchClient(transporter, config)

        self.assertIsInstance(client, SearchClient)

    def test_init_index(self):
        config = SearchConfig('foo', 'bar')
        requester = Requester()
        transporter = Transporter(requester, config)
        client = SearchClient(transporter, config)

        index = client.init_index('foo')

        self.assertIsInstance(index, SearchIndex)

    def test_app_id_getter(self):
        client = SearchClient.create('foo', 'bar')

        self.assertEqual(client.app_id, 'foo')
