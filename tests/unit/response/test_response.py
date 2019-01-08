import unittest

from algoliasearch.responses import Response


class TestResponse(unittest.TestCase):
    def test_dict_access(self):
        response = {
            'foo': 'bar',
        }

        response = FooResponse({}, response)
        self.assertEqual(response['foo'], 'bar')


class FooResponse(Response):
    def wait(self):
        pass
