import unittest

import mock

from algoliasearch.exceptions import RequestException
from algoliasearch.responses import IndexingResponse
from algoliasearch.search_client import SearchClient


class TestResponses(unittest.TestCase):
    def setUp(self):
        self.client = SearchClient.create('foo', 'bar')
        self.client._SearchClient__transporter.write = mock.Mock(name='write')
        self.client._SearchClient__transporter.write.return_value = {}

    def test_dict_access(self):
        response = {
            'foo': 'bar',
        }

        index = self.client.init_index('foo')
        response = IndexingResponse(index, [response])
        self.assertEqual(response.raw_responses[0]['foo'], 'bar')

    def test_request_exception(self):
        self.client.get_user_id = mock.Mock(name="get_user_id")
        self.client.get_user_id.side_effect = RequestException('', 300)

        with self.assertRaises(RequestException) as cm:
            self.client.assign_user_id('foo', 'bar').wait()
        self.assertEqual(cm.exception.status_code, 300)

        with self.assertRaises(RequestException) as cm:
            self.client.remove_user_id('foo').wait()

        self.assertEqual(cm.exception.status_code, 300)

        self.client.get_api_key = mock.Mock(name="get_user_id")
        self.client.get_api_key.side_effect = RequestException('', 300)

        with self.assertRaises(RequestException) as cm:
            self.client.restore_api_key('foo').wait()

        self.assertEqual(cm.exception.status_code, 300)

        self.client._SearchClient__transporter.write.return_value = {
            'key': 'foo'
        }

        with self.assertRaises(RequestException) as cm:
            self.client.add_api_key(['search']).wait()

        self.assertEqual(cm.exception.status_code, 300)
