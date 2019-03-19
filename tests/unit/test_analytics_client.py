import unittest

from algoliasearch.analytics_client import AnalyticsClient
from algoliasearch.configs import SearchConfig
from algoliasearch.exceptions import AlgoliaException


class TestAnalyticsClient(unittest.TestCase):
    def setUp(self):
        self.client = AnalyticsClient.create('foo', 'bar')

    def test_create(self):
        self.assertIsInstance(self.client, AnalyticsClient)
        with self.assertRaises(AssertionError) as _:
            AnalyticsClient.create('', '')

    def test_create_with_config(self):
        config = SearchConfig('foo', 'bar')

        self.assertIsInstance(
            AnalyticsClient.create_with_config(config),
            AnalyticsClient
        )

    def test_get_ab_test(self):
        with self.assertRaises(AssertionError) as _:
            self.client.get_ab_test('')

    def test_stop_ab_test(self):
        with self.assertRaises(AssertionError) as _:
            self.client.stop_ab_test('')

    def test_delete_ab_test(self):
        with self.assertRaises(AssertionError) as _:
            self.client.delete_ab_test('')

    def test_region(self):
        client = AnalyticsClient.create('foo', 'bar')

        self.assertEqual(
            client._config._region, 'us')

        client = AnalyticsClient.create('foo', 'bar', 'fr')

        self.assertEqual(
            client._config._region, 'fr')
