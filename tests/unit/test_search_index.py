import unittest

from algoliasearch.search_client import SearchClient
from algoliasearch.search_index import SearchIndex
from algoliasearch.configs import SearchConfig
from algoliasearch.http.transporter import Transporter
from algoliasearch.http.requester import Requester


class TestSearchIndex(unittest.TestCase):
    def test_init(self):
        config = SearchConfig('foo', 'bar')
        requester = Requester()
        transporter = Transporter(requester, config)
        index = SearchIndex(transporter, config, 'foo')

        self.assertIsInstance(index, SearchIndex)

    def test_app_id_getter(self):
        index = SearchClient.create('foo', 'bar').init_index('index')

        self.assertEqual(index.app_id, 'foo')
