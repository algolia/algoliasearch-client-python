import unittest
import mock as mock

from algoliasearch.config.search_config import SearchConfig
from algoliasearch.http.request_options import RequestOptions
from algoliasearch.http.requester import Requester
from algoliasearch.http.transporter import Transporter


class TestTransporter(unittest.TestCase):
    def setUp(self):
        self.requester = Requester()
        self.requester.request = mock.Mock(name="request")
        self.requester.request.return_value = {}

        self.data = {
            'data': 'foo'
        }

        config = SearchConfig('foo', 'bar')

        self.request_options = RequestOptions.create(config, {
            'User-Agent': 'foo',
            'createIfNotExists': True,
            'readTimeout': 10,
            'bodyParam': 'bar'
        })

        self.transporter = Transporter(self.requester, config)

    def test_write(self):
        self.transporter.write('post', 'endpoint/foo', self.data,
                               self.request_options)

        self.requester.request.assert_called_once_with(
            'POST',  # Upper case letters
            'https://foo-1.algolianet.com/endpoint/foo?createIfNotExists=True',
            self.request_options.headers,
            self.data
        )

    def test_read(self):
        self.transporter.read('get', 'endpoint/bar', self.request_options)

        self.requester.request.assert_called_once_with(
            'GET',  # Upper case letters
            'https://foo-1.algolianet.com/endpoint/bar?createIfNotExists=True',
            self.request_options.headers,
            {}
        )
