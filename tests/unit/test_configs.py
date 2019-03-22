import os
import unittest
from platform import python_version

from algoliasearch.configs import SearchConfig, Config
from algoliasearch.http.hosts import HostsCollection
from algoliasearch.version import VERSION


class TestConfig(unittest.TestCase):
    def setUp(self):
        self.config = SearchConfig('foo', 'bar')

    def test_credentials_from_env(self):
        old_app_id = os.environ.get('ALGOLIA_APP_ID')
        old_api_key = os.environ.get('ALGOLIA_API_KEY')

        try:
            os.environ['ALGOLIA_APP_ID'] = 'foo-1'
            os.environ['ALGOLIA_API_KEY'] = 'bar-1'

            config = FakeConfig()
            self.assertEqual(config.app_id, 'foo-1')
            self.assertEqual(config.api_key, 'bar-1')

            config = FakeConfig('foo-2', 'bar-2')
            self.assertEqual(config.app_id, 'foo-2')
            self.assertEqual(config.api_key, 'bar-2')
        finally:
            if old_app_id:
                os.environ['ALGOLIA_APP_ID'] = old_app_id

            if old_api_key:
                os.environ['ALGOLIA_API_KEY'] = old_api_key

    def test_app_id(self):
        self.assertEqual(self.config.app_id, 'foo')

    def test_api_key(self):
        self.assertEqual(self.config.api_key, 'bar')

    def test_read_timeout(self):
        self.assertEqual(self.config.read_timeout, 5)

    def test_write_timeout(self):
        self.assertEqual(self.config.write_timeout, 30)

    def test_connect_timeout(self):
        self.assertEqual(self.config.connect_timeout, 2)

    def test_wait_task_time_before_retry(self):
        self.assertEqual(self.config.wait_task_time_before_retry, 100000)

    def test_headers(self):
        version = str(python_version())  # type: ignore

        self.assertEqual(self.config.headers, {
            'X-Algolia-Application-Id': 'foo',
            'X-Algolia-API-Key': 'bar',
            'User-Agent': 'Algolia for Python ({}); Python ({})'.format(
                VERSION, version),
            'Content-Type': 'application/json',
        })


class FakeConfig(Config):
    def build_hosts(self):
        pass


class TestSearchConfig(unittest.TestCase):
    def setUp(self):
        self.config = SearchConfig('foo', 'bar')

    def test_batch_size(self):
        self.assertEqual(self.config.batch_size, 1000)

    def test_hosts(self):
        self.assertIsInstance(self.config.hosts.write(), list)
        self.assertIsInstance(self.config.hosts.read(), list)

        # Assert that hosts here assigned.
        self.assertNotEqual(
            len(self.config.hosts.write()), 0
        )
        self.assertNotEqual(
            len(self.config.hosts.read()), 0
        )
