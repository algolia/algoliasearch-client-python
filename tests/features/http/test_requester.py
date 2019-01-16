import unittest

from algoliasearch.exceptions import AlgoliaUnreachableHostException
from tests.helpers.factory import Factory


class TestRequester(unittest.TestCase):
    def setUp(self):
        self.index = Factory.index(self._testMethodName)
        self.obj = Factory.obj()

    def test_timeout(self):
        with self.assertRaises(AlgoliaUnreachableHostException) as _:
            self.index.save_object(self.obj, {'writeTimeout': 0.0001})
