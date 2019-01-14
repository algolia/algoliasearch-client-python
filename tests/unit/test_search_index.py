import unittest

import mock

from algoliasearch.exceptions import MissingObjectIdException
from algoliasearch.http.request_options import RequestOptions
from algoliasearch.search_index import SearchIndex
from algoliasearch.configs import SearchConfig
from algoliasearch.http.transporter import Transporter
from algoliasearch.http.requester import Requester


class TestSearchIndex(unittest.TestCase):
    def setUp(self):
        self.config = SearchConfig('foo', 'bar')
        requester = Requester()
        self.transporter = Transporter(requester, self.config)
        self.transporter.read = mock.Mock(name="read")
        self.transporter.read.return_value = {}
        self.transporter.write = mock.Mock(name="write")
        self.transporter.write.return_value = {}
        self.index = SearchIndex(self.transporter, self.config, 'foo')

    def test_app_id_getter(self):
        self.assertEqual(self.index.app_id, 'foo')

    def test_save_objects(self):
        # Saving an object without object id
        with self.assertRaises(MissingObjectIdException) as _:
            self.index.save_objects([{'foo': 'bar'}])

        with self.assertRaises(MissingObjectIdException) as _:
            self.index.save_objects([{'foo': 'bar'}],
                                    {'autoGenerateObjectIDIfNotExist': False})

        self.index.save_objects([{'foo': 'bar'}],
                                {'autoGenerateObjectIDIfNotExist': True})

        self.transporter.write.assert_called_once_with(
            'POST',
            '1/indexes/foo/batch',
            {'requests': [{'action': 'addObject', 'body': {'foo': 'bar'}}]},
            {},
        )

        self.transporter.write = mock.Mock(name="write")
        self.index.save_objects([{'foo': 'bar', 'objectID': 'foo'}])

        self.transporter.write.assert_called_once_with(
            'POST',
            '1/indexes/foo/batch',
            {
                'requests': [
                    {
                        'action': 'updateObject',
                        'body': {'foo': 'bar', 'objectID': 'foo'}}
                ]
            }, None
        )

    def test_partial_update_objects(self):
        # Saving an object without object id
        with self.assertRaises(MissingObjectIdException) as _:
            self.index.partial_update_objects([{'foo': 'bar'}])

        with self.assertRaises(MissingObjectIdException) as _:
            self.index.partial_update_objects([{'foo': 'bar'}],
                                              {'createIfNotExists': False})

        self.index.partial_update_objects([{'foo': 'bar'}],
                                          {'createIfNotExists': True})

        self.transporter.write.assert_called_once_with(
            'POST', '1/indexes/foo/batch',
            {'requests': [
                {'action': 'partialUpdateObject', 'body': {'foo': 'bar'}}]},
            {},
        )

        self.transporter.write = mock.Mock(name="write")

        self.index.partial_update_objects([{'foo': 'bar', 'objectID': 'foo'}])

        self.transporter.write.assert_called_once_with(
            'POST', '1/indexes/foo/batch',
            {
                'requests': [
                    {
                        'action': 'partialUpdateObjectNoCreate',
                        'body': {'foo': 'bar', 'objectID': 'foo'}
                    }
                ]
            },
            None,
        )
