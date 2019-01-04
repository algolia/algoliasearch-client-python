import unittest

from algoliasearch.config.search_config import SearchConfig
from algoliasearch.http.request_options import RequestOptions


class TestRequestOptions(unittest.TestCase):
    def setUp(self):
        self.config = SearchConfig('foo', 'bar')

        self.request_options = RequestOptions.create(self.config, {

            # Headers
            'User-Agent': 'foo',

            # Query Params
            'createIfNotExists': True,

            # Timeouts Params
            'readTimeout': 10,

            # Data Params
            'bodyParam': 'bar'
        })

    def test_with_options(self):
        self.assertIsInstance(RequestOptions.create(self.config),
                              RequestOptions)

    def test_headers(self):
        self.assertEqual(self.request_options.headers['User-Agent'], 'foo')

        # Default Value
        self.assertEqual(self.request_options.headers['Content-Type'],
                         'application/json')

    def test_query_parameters(self):
        create_if_not_exists = self.request_options.query_parameters[
            'createIfNotExists']
        self.assertEqual(create_if_not_exists, True)

        # Default Behavior
        self.assertTrue(
            'forwardToReplicas' not in self.request_options.query_parameters
        )

    def test_timeouts(self):
        read_timeout = self.request_options.timeouts['readTimeout']
        self.assertEqual(read_timeout, 10)

        # Default Value
        default_timeout = self.request_options.timeouts['connectTimeout']
        self.assertEqual(default_timeout, 5)

    def test_data(self):
        self.assertEqual(
            self.request_options.data['bodyParam'], 'bar')
