import unittest

from algoliasearch.configs import SearchConfig
from algoliasearch.http.request_options import RequestOptions
from algoliasearch.user_agent import UserAgent


class TestRequestOptions(unittest.TestCase):
    def setUp(self):
        self.config = SearchConfig('foo', 'bar')
        self.config.headers['Foo-Bar'] = 'foo-bar'

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

    def test_default_user_agent(self):
        self.assertEqual(
            RequestOptions.create(self.config).headers['User-Agent'],
            UserAgent.get()
        )

    def test_headers(self):
        self.assertEqual(self.request_options.headers['User-Agent'], 'foo')

        # Default Value
        self.assertEqual(self.request_options.headers['Content-Type'],
                         'application/json')

        # Custom header set on the config
        self.assertEqual(self.request_options.headers['Foo-Bar'],
                         'foo-bar')

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
        default_timeout = self.request_options.timeouts['writeTimeout']
        self.assertEqual(default_timeout, 30)

    def test_data(self):
        self.assertEqual(
            self.request_options.data['bodyParam'], 'bar')
