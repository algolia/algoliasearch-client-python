import unittest

import mock

from algoliasearch.recommend_client import RecommendClient
from algoliasearch.configs import SearchConfig
from algoliasearch.http.transporter import Transporter
from algoliasearch.http.requester import Requester


class TestRecommendClient(unittest.TestCase):
    def setUp(self):
        self.config = SearchConfig("foo", "bar")
        self.transporter = Transporter(Requester(), self.config)
        self.transporter.read = mock.Mock(name="read")
        self.transporter.read.return_value = {}
        self.transporter.write = mock.Mock(name="write")
        self.transporter.write.return_value = {}

        self.client = RecommendClient(self.transporter, self.config)

    def test_create(self):
        self.assertIsInstance(self.client, RecommendClient)
        with self.assertRaises(AssertionError) as _:
            RecommendClient.create("", "")

    def test_create_with_config(self):
        config = SearchConfig("foo", "bar")

        self.assertIsInstance(
            RecommendClient.create_with_config(config), RecommendClient
        )

    def test_app_id_getter(self):
        client = RecommendClient.create("foo", "bar")

        self.assertEqual(client.app_id, "foo")
