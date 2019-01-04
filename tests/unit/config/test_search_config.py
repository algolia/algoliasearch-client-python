import unittest

from algoliasearch.config.search_config import SearchConfig
from algoliasearch.http.hosts_collection import HostsCollection


class TestSearchConfig(unittest.TestCase):
    def setUp(self):
        self.config = SearchConfig('foo', 'bar')

    def test_hosts(self):
        self.assertIsInstance(self.config.hosts, HostsCollection)

        # Assert that hosts here assigned.
        self.assertNotEqual(len(self.config.hosts.write), 0)
        self.assertNotEqual(len(self.config.hosts.read), 0)
