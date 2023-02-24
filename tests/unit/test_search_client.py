import unittest

import mock

from algoliasearch.configs import SearchConfig
from algoliasearch.http.requester import Requester
from algoliasearch.http.transporter import Transporter
from algoliasearch.search_client import SearchClient
from algoliasearch.search_index import SearchIndex


class TestSearchClient(unittest.TestCase):
    def setUp(self):
        self.config = SearchConfig("foo", "bar")
        self.transporter = Transporter(Requester(), self.config)
        self.transporter.read = mock.Mock(name="read")
        self.transporter.read.return_value = {}
        self.transporter.write = mock.Mock(name="write")
        self.transporter.write.return_value = {}

        self.client = SearchClient(self.transporter, self.config)

    def test_create(self):
        self.assertIsInstance(self.client, SearchClient)
        with self.assertRaises(AssertionError) as _:
            SearchClient.create("", "")

    def test_create_with_config(self):
        config = SearchConfig("foo", "bar")

        self.assertIsInstance(SearchClient.create_with_config(config), SearchClient)

    def test_init_index(self):
        index = self.client.init_index("foo")

        self.assertIsInstance(index, SearchIndex)

    def test_app_id_getter(self):
        client = SearchClient.create("foo", "bar")

        self.assertEqual(client.app_id, "foo")
