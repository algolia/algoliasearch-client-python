import unittest

import mock

from algoliasearch.exceptions import RequestException, MissingObjectIdException
from algoliasearch.http.request_options import RequestOptions
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

    def test_exists(self):

        with mock.patch.object(self.index, 'get_settings') as submethod_mock:
            submethod_mock.side_effect = RequestException(
                "Index does not exist", 404
            )

            indexExists = self.index.exists()

            self.index.get_settings.assert_called_once()

            # No request options
            args = self.index.get_settings.call_args[0]
            self.assertEqual(args[0], None)

            self.assertEqual(indexExists, False)

        with mock.patch.object(self.index, 'get_settings') as submethod_mock:
            submethod_mock.side_effect = RequestException(
                "Permissions error", 400
            )

            with self.assertRaises(RequestException) as _:
                self.index.exists()

        with mock.patch.object(self.index, 'get_settings') as submethod_mock:
            submethod_mock.return_value = {
                'hitsPerPage': 20,
                'maxValuesPerFacet': 100
            }

            request_options = {
                'X-Algolia-User-ID': 'Foo'
            }

            indexExists = self.index.exists(request_options)

            # With request options
            args = self.index.get_settings.call_args[0]
            self.assertEqual(args[0], request_options)

            self.index.get_settings.assert_called_once()
            self.assertEqual(indexExists, True)

        with mock.patch.object(self.index, 'get_settings') as submethod_mock:
            submethod_mock.return_value = {
                'hitsPerPage': 20,
                'maxValuesPerFacet': 100
            }

            indexExists = self.index.exists()

            self.index.get_settings.assert_called_once()
            self.assertEqual(indexExists, True)

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

    def test_get_objects(self):
        request_options = RequestOptions.create(self.config)

        requests = [{
            'indexName': 'index-name',
            'objectID': 'foo_id'
        }]

        self.index.get_objects(['foo_id'], request_options)

        self.transporter.read.assert_called_once_with(
            'POST',
            '1/indexes/*/objects',
            {'requests': requests},  # asserts version 2 it's used.
            request_options
        )

    def test_get_objects_with_attributes_to_retreive(self):
        request_options = RequestOptions.create(self.config, {
            'attributesToRetrieve': ['firstname', 'lastname']
        })

        requests = [{
            'indexName': 'index-name',
            'objectID': 'foo_id',
            'attributesToRetrieve': ['firstname', 'lastname']
        }]

        self.index.get_objects(['foo_id'], request_options)

        self.transporter.read.assert_called_once_with(
            'POST',
            '1/indexes/*/objects',
            {'requests': requests},  # asserts version 2 it's used.
            request_options
        )

        self.assertNotIn('attributesToRetrieve', request_options.data)

    def test_get_objects_with_attributes_to_retreive_bulk(self):
        request_options = RequestOptions.create(self.config, {
            'attributesToRetrieve': ['firstname', 'lastname']
        })

        requests = [{
            'indexName': 'index-name',
            'objectID': 'foo_id',
            'attributesToRetrieve': ['firstname', 'lastname']
        }, {
            'indexName': 'index-name',
            'objectID': 'bar_id',
            'attributesToRetrieve': ['firstname', 'lastname']
        }]

        self.index.get_objects(['foo_id', 'bar_id'], request_options)

        self.transporter.read.assert_called_once_with(
            'POST',
            '1/indexes/*/objects',
            {'requests': requests},  # asserts version 2 it's used.
            request_options
        )

        self.assertNotIn('attributesToRetrieve', request_options.data)

    def test_get_settings(self):
        self.transporter.read.return_value = {
            'attributesToIndex': ['attr1', 'attr2'],
            'numericAttributesToIndex': ['attr1', 'attr2'],
            'slaves': ['index1', 'index2'],
            'ignorePlurals': True,
        }

        request_options = RequestOptions.create(self.config, {'foo': 'bar'})
        settings = self.index.get_settings(request_options)

        self.transporter.read.assert_called_once_with(
            'GET',
            '1/indexes/index-name/settings',
            None,
            request_options
        )

        self.assertEqual(request_options.query_parameters['getVersion'], 2)

        self.assertEqual(settings, {
            'searchableAttributes': ['attr1', 'attr2'],
            'numericAttributesForFiltering': ['attr1', 'attr2'],
            'replicas': ['index1', 'index2'],
            'ignorePlurals': True,
        })

    def test_get_settings_none_as_request_options(self):
        self.index.get_settings()

        args = self.transporter.read.call_args[0]

        self.assertEqual(args[3].query_parameters['getVersion'], 2)

    def test_get_settings_dict_as_request_options(self):
        self.index.get_settings({'foo': 'bar'})

        args = self.transporter.read.call_args[0]

        self.assertEqual(args[3].query_parameters['getVersion'], 2)

    def test_get_settings_with_request_options(self):
        request_options = RequestOptions.create(self.config, {'foo': 'bar'})

        self.index.get_settings(request_options)

        args = self.transporter.read.call_args[0]

        self.assertEqual(args[3].query_parameters['getVersion'], 2)

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

    def test_find_object(self):
        self.index.search = mock.Mock(name="search")
        self.index.search.return_value = {
            'hits': [{'foo': 'bar'}],
            'nbPages': 1
        }

        self.index.find_object(lambda obj: True)
        args, _ = self.index.search.call_args
        self.assertEqual(args[0], '')
        self.assertEqual(args[1].data,
                         RequestOptions.create(self.config, {'page': 0}).data)

        self.index.find_object(lambda obj: True, {
            'query': 'foo',
            'hitsPerPage': 5
        })
        args, _ = self.index.search.call_args
        self.assertEqual(args[0], 'foo')
        self.assertEqual(args[1].data, RequestOptions.create(self.config, {
            'hitsPerPage': 5,
            'page': 0
        }).data)

        self.index.find_object(lambda obj: True, RequestOptions.create(
            self.config, {
                'User-Agent': 'blabla'
            }
        ))
        args, _ = self.index.search.call_args
        self.assertEqual(args[0], '')
        self.assertEqual(args[1].data, RequestOptions.create(self.config, {
            'page': 0
        }).data)

        self.assertEqual(args[1].headers, RequestOptions.create(self.config, {
            'User-Agent': 'blabla'
        }).headers)

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
