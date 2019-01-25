import unittest

from algoliasearch.insights_client import InsightsClient


class TestInsightsClient(unittest.TestCase):
    def test_create(self):
        client = InsightsClient.create('foo', 'bar')

        self.assertIsInstance(client, InsightsClient)

    def test_region(self):
        client = InsightsClient.create('foo', 'bar')

        self.assertEqual(
            client._InsightsClient__config._InsightsConfig__region, 'us')

        client = InsightsClient.create('foo', 'bar', 'fr')

        self.assertEqual(
            client._InsightsClient__config._InsightsConfig__region, 'fr')
