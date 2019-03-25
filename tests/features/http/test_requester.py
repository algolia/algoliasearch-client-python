import unittest

from algoliasearch.exceptions import AlgoliaUnreachableHostException, \
    RequestException
from tests.helpers.factory import Factory


class TestRequester(unittest.TestCase):
    def setUp(self):
        self.index = Factory.index(self._testMethodName)
        self.obj = Factory.obj()

    def test_timeout_exception(self):
        with self.assertRaises(AlgoliaUnreachableHostException) as _:
            self.index.save_object(self.obj, {'writeTimeout': 0.0001})

    def test_http_error_exception(self):
        with self.assertRaises(RequestException) as cm:
            self.index.set_settings({'zadaz': 'zadza'})

        exception = cm.exception
        self.assertEqual(exception.status_code, 400)
        self.assertEqual(
            str(exception),
            'Invalid object attributes: zadaz near line:1 column:8'
        )
