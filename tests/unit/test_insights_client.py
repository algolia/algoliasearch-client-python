import unittest

from algoliasearch.configs import InsightsConfig
from algoliasearch.exceptions import AlgoliaException
from algoliasearch.insights_client import InsightsClient


class TestInsightsClient(unittest.TestCase):
    def test_create(self):
        client = InsightsClient.create('foo', 'bar')

        self.assertIsInstance(client, InsightsClient)
        with self.assertRaises(AssertionError) as _:
            InsightsClient.create('', '')

    def test_create_with_config(self):
        config = InsightsConfig('foo', 'bar')

        self.assertIsInstance(
            InsightsClient.create_with_config(config),
            InsightsClient
        )

    def test_region(self):
        client = InsightsClient.create('foo', 'bar')

        self.assertEqual(
            client._config._region, 'us')

        client = InsightsClient.create('foo', 'bar', 'fr')

        self.assertEqual(
            client._config._region, 'fr')
