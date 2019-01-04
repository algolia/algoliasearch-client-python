import unittest

from algoliasearch.config.search_config import SearchConfig
from algoliasearch.http.hosts_collection import HostsCollection


class TestConfig(unittest.TestCase):
    def setUp(self):
        self.config = SearchConfig('foo', 'bar')

    def test_app_id(self):
        self.assertEqual(self.config.app_id, 'foo')

    def test_api_key(self):
        self.assertEqual(self.config.api_key, 'bar')

    def test_read_timeout(self):
        self.assertEqual(self.config.read_timeout, 5)

    def test_write_timeout(self):
        self.assertEqual(self.config.write_timeout, 5)

    def test_connect_timeout(self):
        self.assertEqual(self.config.connect_timeout, 5)
