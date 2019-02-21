import unittest

from algoliasearch.analytics_client import AnalyticsClient


class TestAnalyticsClient(unittest.TestCase):
    def setUp(self):
        self.client = AnalyticsClient.create('foo', 'bar')

    def test_create(self):
        self.assertIsInstance(self.client, AnalyticsClient)

    def test_get_ab_test(self):
        with self.assertRaises(ValueError) as _:
            self.client.get_ab_test('')

    def test_stop_ab_test(self):
        with self.assertRaises(ValueError) as _:
            self.client.stop_ab_test('')

    def test_delete_ab_test(self):
        with self.assertRaises(ValueError) as _:
            self.client.delete_ab_test('')

    def test_region(self):
        client = AnalyticsClient.create('foo', 'bar')

        self.assertEqual(
            client._AnalyticsClient__config._AnalyticsConfig__region, 'us')

        client = AnalyticsClient.create('foo', 'bar', 'fr')

        self.assertEqual(
            client._AnalyticsClient__config._AnalyticsConfig__region, 'fr')
