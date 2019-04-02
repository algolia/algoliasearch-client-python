import unittest

import mock

from algoliasearch.exceptions import RequestException
from algoliasearch.responses import (
    IndexingResponse, MultipleResponse,
    AddApiKeyResponse, UpdateApiKeyResponse,
    DeleteApiKeyResponse, MultipleIndexBatchIndexingResponse
)
from algoliasearch.search_client import SearchClient


class TestResponses(unittest.TestCase):
    def setUp(self):
        self.client = SearchClient.create('foo', 'bar')
        self.client._transporter.write = mock.Mock(name='write')
        self.client._transporter.write.return_value = {}

    def test_dict_access(self):
        response = {
            'foo': 'bar',
        }

        response_object = IndexingResponse({}, [response])
        self.assertEqual(response_object[0]['foo'], 'bar')

        response_object = MultipleResponse([response])
        self.assertEqual(response_object[0]['foo'], 'bar')

        response_object = MultipleResponse([IndexingResponse({}, [response])])
        self.assertEqual(response_object[0][0]['foo'], 'bar')

        response_object = AddApiKeyResponse({}, response)
        self.assertEqual(response_object['foo'], 'bar')

        response_object = UpdateApiKeyResponse({}, response, {})
        self.assertEqual(response_object['foo'], 'bar')

        response_object = DeleteApiKeyResponse({}, response, '')
        self.assertEqual(response_object['foo'], 'bar')

        response_object = MultipleIndexBatchIndexingResponse({}, response)
        self.assertEqual(response_object['foo'], 'bar')

    def test_request_exception(self):
        self.client._transporter.write.side_effect = RequestException('', 300)

        with self.assertRaises(RequestException) as cm:
            self.client.assign_user_id('foo', 'bar')
        self.assertEqual(cm.exception.status_code, 300)

        with self.assertRaises(RequestException) as cm:
            self.client.remove_user_id('foo')
        self.assertEqual(cm.exception.status_code, 300)

        with self.assertRaises(RequestException) as cm:
            self.client.restore_api_key('foo')
        self.assertEqual(cm.exception.status_code, 300)

        with self.assertRaises(RequestException) as cm:
            self.client.add_api_key(['search']).wait()
        self.assertEqual(cm.exception.status_code, 300)
