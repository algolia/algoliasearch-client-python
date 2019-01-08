import time
import unittest

from algoliasearch.http.hosts import Host


class TestHost(unittest.TestCase):
    def setUp(self):
        self.host = Host('foo.com')

    def test_url(self):
        self.assertEqual(self.host.url, 'foo.com')

    def test_priority(self):
        # Default priority test
        self.assertEqual(self.host.priority, 0)

        host_with_less_priority = Host('foo.com', 5)
        # Specific priority
        self.assertEqual(host_with_less_priority.priority, 5)

    def test_up(self):
        self.assertEqual(self.host.up, True)

    def test_last_use(self):
        self.assertEqual(self.host.last_use, 0)

    def test_retry_count(self):
        self.assertEqual(self.host.retry_count, 0)

    def test_reset(self):
        self.host.up = False
        self.host.last_use = time.time()
        self.host.retry_count = 3

        self.host.reset()

        self.assertEqual(self.host.up, True)
        self.assertEqual(self.host.last_use, 0)
        self.assertEqual(self.host.retry_count, 0)
