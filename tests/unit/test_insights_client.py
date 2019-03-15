import unittest

from algoliasearch.exceptions import AlgoliaException
from algoliasearch.insights_client import InsightsClient


class TestInsightsClient(unittest.TestCase):
    def test_create(self):
        client = InsightsClient.create('foo', 'bar')

        self.assertIsInstance(client, InsightsClient)
        with self.assertRaises(AssertionError) as _:
            InsightsClient.create('', '')

    def test_region(self):
        client = InsightsClient.create('foo', 'bar')

        self.assertEqual(
            client._config._InsightsConfig__region, 'us')

        client = InsightsClient.create('foo', 'bar', 'fr')

        self.assertEqual(
            client._config._InsightsConfig__region, 'fr')
