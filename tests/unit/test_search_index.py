import unittest

import mock

from algoliasearch.exceptions import MissingObjectIdException
from algoliasearch.responses import Response
from algoliasearch.search_index import SearchIndex
from algoliasearch.configs import SearchConfig
from algoliasearch.http.transporter import Transporter
from algoliasearch.http.requester import Requester
from tests.helpers.factory import Factory as F


class TestSearchIndex(unittest.TestCase):
    def setUp(self):
        self.config = SearchConfig('foo', 'bar')
        requester = Requester()
        self.transporter = Transporter(requester, self.config)
        self.transporter.read = mock.Mock(name="read")
        self.transporter.read.return_value = {}
        self.transporter.write = mock.Mock(name="write")
        self.transporter.write.return_value = {}
        self.index = SearchIndex(self.transporter, self.config, 'index-name')

    def test_app_id_getter(self):
        self.assertEqual(self.index.app_id, 'foo')

    def test_name_getter(self):
        self.assertEqual(self.index.name, 'index-name')

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
            '1/indexes/index-name/batch',
            {'requests': [{'action': 'addObject', 'body': {'foo': 'bar'}}]},
            {},
        )

        self.transporter.write = mock.Mock(name="write")
        self.index.save_objects([{'foo': 'bar', 'objectID': 'foo'}])

        self.transporter.write.assert_called_once_with(
            'POST',
            '1/indexes/index-name/batch',
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
            'POST', '1/indexes/index-name/batch',
            {'requests': [
                {'action': 'partialUpdateObject', 'body': {'foo': 'bar'}}]},
            {},
        )

        self.transporter.write = mock.Mock(name="write")

        self.index.partial_update_objects([{'foo': 'bar', 'objectID': 'foo'}])

        self.transporter.write.assert_called_once_with(
            'POST', '1/indexes/index-name/batch',
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

    def test_get_settings(self):
        self.transporter.read.return_value = {
            'attributesToIndex': ['attr1', 'attr2'],
            'numericAttributesToIndex': ['attr1', 'attr2'],
            'slaves': ['index1', 'index2'],
            'ignorePlurals': True,
        }

        settings = self.index.get_settings({'foo': 'bar'})

        self.transporter.read.assert_called_once_with(
            'GET',
            '1/indexes/index-name/settings',
            {'getVersion': 2},  # asserts version 2 it's used.
            {'foo': 'bar'}
        )

        self.assertEqual(settings, {
            'searchableAttributes': ['attr1', 'attr2'],
            'numericAttributesForFiltering': ['attr1', 'attr2'],
            'replicas': ['index1', 'index2'],
            'ignorePlurals': True,
        })

    def test_save_synonyms(self):
        # Test null response
        self.index.save_synonyms([]).wait()

        # Test object id validation
        with self.assertRaises(MissingObjectIdException) as _:
            self.index.save_synonyms([F.synonym(object_id=False)])

        # Test object id validation
        with self.assertRaises(MissingObjectIdException) as _:
            self.index.save_synonym(F.synonym(object_id=False))

    def test_save_rules(self):
        # Test null response
        self.index.save_rules([]).wait()

        # Test object id validation
        with self.assertRaises(MissingObjectIdException) as _:
            self.index.save_rule({'foo': 'bar'})

        # Test object id validation
        with self.assertRaises(MissingObjectIdException) as _:
            self.index.save_rules([{'foo': 'bar'}])

    def test_replace_all_objects(self):
        self.index._create_temporary_name = mock.Mock(
            name="_create_temporary_name")
        tmp_index_name = 'index-name_tmp_bar'
        self.index._create_temporary_name.return_value = tmp_index_name  # noqa: E501

        obj = F.obj()
        self.index.replace_all_objects([obj])

        # Asserts the operations of the replace all objects.
        self.transporter.write.assert_has_calls(
            [mock.call('POST', '1/indexes/index-name/operation',
                       {'operation': 'copy',
                        'destination': 'index-name_tmp_bar'},
                       {'scope': ['settings', 'synonyms', 'rules']}),
             mock.call('POST', '1/indexes/index-name_tmp_bar/batch',
                       {'requests': [
                           {'action': 'updateObject', 'body': obj}]}, None),
             mock.call('POST', '1/indexes/index-name_tmp_bar/operation',
                       {'operation': 'move', 'destination': 'index-name'},
                       None)]
        )

        response = NullResponse()
        response.wait = mock.Mock(name="wait")

        self.index.copy_to = mock.Mock(
            name="copy_to")
        self.index.copy_to.return_value = response

        self.index.move_to = mock.Mock(
            name="move_to")
        self.index.move_to.return_value = response

        self.index.save_objects = mock.Mock(
            name="save_objects")
        self.index.save_objects.return_value = response

        self.index.replace_all_objects([obj])
        self.assertEqual(response.wait.call_count, 0)

        result = self.index.replace_all_objects([obj], {'safe': True})
        self.assertEqual(response.wait.call_count, 3)
        self.assertEqual(len(result.responses), 3)
        self.assertEqual(len(result._waitable), 0)

    def test_get_task(self):
        with self.assertRaises(AssertionError) as _:
            self.index.get_task('')


class NullResponse(Response):

    def wait(self):
        return self
