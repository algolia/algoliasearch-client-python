# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import calendar
from random import randint
from decimal import Decimal
from datetime import datetime

try:
    import unittest2 as unittest  # py26
except ImportError:
    import unittest

from algoliasearch.client import MAX_API_KEY_LENGTH
from algoliasearch.helpers import AlgoliaException

from tests.helpers import safe_index_name
from tests.helpers import get_api_client
from tests.helpers import FakeData


class IndexTest(unittest.TestCase):
    """Abstract class for all index tests."""

    @classmethod
    def setUpClass(cls):
        cls.client = get_api_client()
        cls.index_name = safe_index_name('àlgol?à-python{0}'.format(
                                         randint(1, 1000)))
        cls.index = cls.client.init_index(cls.index_name)
        cls.client.delete_index(cls.index_name)

        cls.factory = FakeData()

    @classmethod
    def tearDownClass(cls):
        cls.client.delete_index(cls.index_name)


class IndexWithoutDataTest(IndexTest):
    """Tests that use one index without initial data."""

    def tearDown(self):
        self.index.clear_index()

    def test_add_object(self):
        obj = self.factory.fake_contact()
        task = self.index.add_object(obj)
        self.index.wait_task(task['taskID'])

        res = self.index.get_object(task['objectID'])
        self.assertDictContainsSubset(obj, res)

    def test_add_object_with_objectID(self):
        obj = self.factory.fake_contact()
        obj['objectID'] = '101'
        task = self.index.add_object(obj, obj['objectID'])
        self.index.wait_task(task['taskID'])

        res = self.index.get_object(obj['objectID'])
        self.assertDictEqual(obj, res)

    def test_add_objects(self):
        objs = self.factory.fake_contact(5)
        task = self.index.add_objects(objs)
        self.index.wait_task(task['taskID'])

        res = self.index.get_objects(task['objectIDs'])
        self.assertEqual(len(res['results']), 5)

        for obj, obj_res in zip(objs, res['results']):
            self.assertDictContainsSubset(obj, obj_res)

    def test_save_object(self):
        obj = self.factory.fake_contact()
        obj['objectID'] = 4242
        task = self.index.save_object(obj)
        self.index.wait_task(task['taskID'])

        res = self.index.get_object(obj['objectID'])
        obj['objectID'] = '4242'  # The backends always returns str(objectID)
        self.assertDictEqual(obj, res)

    def test_save_objects(self):
        objs = self.factory.fake_contact(5)
        objectIDs = []
        for obj in objs:
            new_id = self.factory.generate_id()
            objectIDs.append(new_id)
            obj['objectID'] = new_id
        task = self.index.save_objects(objs)
        self.index.wait_task(task['taskID'])

        res = self.index.get_objects(objectIDs)
        for obj, obj_res in zip(objs, res['results']):
            self.assertDictEqual(obj, obj_res)

    def test_encode_decimal(self):
        value = Decimal('3.14')
        task = self.index.add_object({'pi': value})
        self.index.wait_task(task['taskID'])

        res = self.index.get_object(task['objectID'])
        self.assertEqual(res['pi'], float(value))

    def test_encode_datetime(self):
        value = datetime.now()
        task = self.index.add_object({'now': value})
        self.index.wait_task(task['taskID'])

        res = self.index.get_object(task['objectID'])
        self.assertEqual(res['now'], calendar.timegm(value.utctimetuple()))

    def test_synonyms(self):
        task = self.index.add_object({'name': '589 Howard St., San Francisco'})
        task = self.index.batch_synonyms([
            {'objectID': 'city', 'type': 'synonym',
             'synonyms': ['San Francisco', 'SF']},
            {'objectID': 'street', 'type': 'altCorrection1',
             'word': 'Street', 'corrections': ['St']}
        ])
        self.index.wait_task(task['taskID'])
        task = self.index.get_synonym("city")
        self.assertEqual('city', task['objectID'])
        task = self.index.search('Howard Street SF')
        self.assertEqual(1, int(task['nbHits']))
        task = self.index.delete_synonym('street')
        self.index.wait_task(task['taskID'])
        task = self.index.search_synonyms('', ['synonym'], 0, 5)
        self.assertEqual(1, int(task['nbHits']))
        task = self.index.clear_synonyms()
        self.index.wait_task(task['taskID'])
        task = self.index.search_synonyms('', hits_per_page=5)
        self.assertEqual(0, int(task['nbHits']))

    def test_facet_search(self):
        settings = {'attributesForFacetting': ['searchable(series)', 'kind']}
        objects = [
             {
                 'objectID': '1',
                 'name': 'Snoopy',
                 'kind': [ 'dog', 'animal' ],
                 'born': 1950,
                 'series': 'Peanuts'
             },
             {
                 'objectID': '2',
                 'name': 'Woodstock',
                 'kind': ['bird', 'animal' ],
                 'born': 1960,
                 'series': 'Peanuts'
             },
             {
                 'objectID': '3',
                 'name': 'Charlie Brown',
                 'kind': [ 'human' ],
                 'born': 1950,
                 'series': 'Peanuts'
             },
            {
                'objectID': '4',
                'name': 'Hobbes',
                'kind': ['tiger', 'animal', 'teddy' ],
                'born': 1985,
                'series': 'Calvin & Hobbes'
            },
            {
                'objectID': '5',
                'name': 'Calvin',
                'kind': [ 'human' ],
                'born': 1985,
                'series': 'Calvin & Hobbes'
             }
         ]

        self.index.set_settings(settings)
        task = self.index.add_objects(objects)
        self.index.wait_task(task['taskID'])

        # Straightforward search.
        facetHits = self.index.search_facet('series', 'Hobb')['facetHits']
        self.assertEqual(len(facetHits), 1)
        self.assertEqual(facetHits[0]['value'], 'Calvin & Hobbes')
        self.assertEqual(facetHits[0]['count'], 2)

        # Using an addition query to restrict search.
        query = {'facetFilters': 'kind:animal', 'numericFilters': 'born >= 1955'}
        facetHits = self.index.search_facet('series', 'Peanutz', query)['facetHits']
        self.assertEqual(facetHits[0]['value'], 'Peanuts')
        self.assertEqual(facetHits[0]['count'], 1)

class IndexWithReadOnlyDataTest(IndexTest):
    """Tests that use one index with initial data (read only)."""

    @classmethod
    def setUpClass(cls):
        super(IndexWithReadOnlyDataTest, cls).setUpClass()

        cls.objs = cls.factory.fake_contact(5)
        task = cls.index.add_objects(cls.objs)
        cls.index.wait_task(task['taskID'])
        cls.objectIDs = task['objectIDs']

    def test_settings(self):
        task = self.index.set_settings({
            'attributesToHighlight': ['name'],
            'minProximity': 2
        })
        self.index.wait_task(task['taskID'])

        res = self.index.get_settings()
        self.assertListEqual(res['attributesToHighlight'], ['name'])

        # reset settings
        task = self.index.set_settings({
            'attributesToHighlight': None,
            'minProximity': 1
        })

    def test_get_object(self):
        res = self.index.get_object(self.objectIDs[3])
        self.assertDictContainsSubset(self.objs[3], res)

        res = self.index.get_object(self.objectIDs[0])
        self.assertDictContainsSubset(self.objs[0], res)

        res = self.index.get_object(self.objectIDs[4])
        self.assertDictContainsSubset(self.objs[4], res)

    def test_get_object_with_attributes_to_retrieve(self):
        res = self.index.get_object(self.objectIDs[3],
                                    attributes_to_retrieve=['name', 'email'])
        self.assertEqual(self.objs[3]['name'], res['name'])
        self.assertEqual(self.objs[3]['email'], res['email'])
        self.assertNotIn('phone', res)
        self.assertNotIn('city', res)
        self.assertNotIn('country', res)

        res = self.index.get_object(self.objectIDs[0],
                                    attributes_to_retrieve='city')
        self.assertNotIn('name', res)
        self.assertNotIn('email', res)
        self.assertNotIn('phone', res)
        self.assertEqual(self.objs[0]['city'], res['city'])
        self.assertNotIn('country', res)

        res = self.index.get_object(self.objectIDs[0],
                                    attributes_to_retrieve='objectID')
        self.assertNotIn('name', res)
        self.assertNotIn('email', res)
        self.assertNotIn('phone', res)
        self.assertNotIn('city', res)
        self.assertNotIn('country', res)

    def test_get_objects(self):
        res = self.index.get_objects(self.objectIDs[1:3])
        for obj, obj_res in zip(self.objs[1:3], res['results']):
            self.assertDictContainsSubset(obj, obj_res)

        res = self.index.get_objects([self.objectIDs[3],
                                      self.objectIDs[0],
                                      self.objectIDs[2]])
        self.assertEqual(len(res['results']), 3)
        self.assertDictContainsSubset(self.objs[3], res['results'][0])
        self.assertDictContainsSubset(self.objs[0], res['results'][1])
        self.assertDictContainsSubset(self.objs[2], res['results'][2])

    def test_get_objects_with_attributes_to_retrieve(self):
        res = self.index.get_objects(self.objectIDs[1:3], attributes_to_retrieve=['name', 'email'])
        for obj, obj_res in zip(self.objs[1:3], res['results']):
            self.assertEqual(obj['name'], obj_res['name'])
            self.assertEqual(obj['email'], obj_res['email'])
            self.assertNotIn('phone', obj_res)
            self.assertNotIn('city', obj_res)
            self.assertNotIn('country', obj_res)

    def test_browse(self):
        res = self.index.browse(page=0, hits_per_page=2)
        self.assertEqual(res['page'], 0)
        self.assertEqual(res['nbHits'], 5)
        self.assertEqual(res['hitsPerPage'], 2)

        for i in range(5):
            res = self.index.browse(page=i, hits_per_page=1)
            self.assertIn(res['hits'][0]['objectID'], self.objectIDs)

    def browse_all(self):
        params = {
            'hitsPerPage': 2,
            'attributesToRetrieve': ['objectID']
        }

        res_ids = []
        it = self.index.browse_all(params)
        for record in it:
            self.assertEqual(len(record.keys()), 1)
            self.assertIn('objectID', record)
            res_ids.append(record['objectID'])

        self.assertEqual(it.answer['nbPages'], 3)
        self.assertEqual(len(res_ids), 5)
        self.assertSetEqual(set(self.objectIDs), set(res_ids))

    def test_search(self):
        res = self.index.search('')
        self.assertEqual(res['nbHits'], 5)

        res = self.index.search('', {'hitsPerPage': 2})
        self.assertEqual(res['nbHits'], 5)
        self.assertEqual(res['hitsPerPage'], 2)

        res = self.index.search('', {
            'attributesToRetrieve': ['name', 'email']
        })
        res_keys = res['hits'][0].keys()
        self.assertIn('name', res_keys)
        self.assertIn('email', res_keys)
        self.assertNotIn('phone', res_keys)
        self.assertNotIn('city', res_keys)
        self.assertNotIn('country', res_keys)

        res = self.index.search('', {
            'attributesToRetrieve': 'name,email'
        })
        res_keys = res['hits'][0].keys()
        self.assertIn('name', res_keys)
        self.assertIn('email', res_keys)
        self.assertNotIn('phone', res_keys)
        self.assertNotIn('city', res_keys)
        self.assertNotIn('country', res_keys)

        res = self.index.search('', {'analytics': False})
        self.assertEqual(res['nbHits'], 5)
        try:
            self.assertRegexpMatches(res['params'], r'analytics=false')
        except AttributeError:
            self.assertRegex(res['params'], r'analytics=false')

        res = self.index.search(self.objs[2]['name'][0])
        self.assertGreaterEqual(res['nbHits'], 1)
        res_ids = [elt['objectID'] for elt in res['hits']]
        self.assertIn(self.objectIDs[2], res_ids)

    def test_search_with_short_secured_api_key(self):
        old_key = self.client.api_key

        secured_api_key = self.client.generate_secured_api_key(
            os.environ['ALGOLIA_API_KEY_SEARCH'],
            dict(filters=''),
        )
        assert len(secured_api_key) < MAX_API_KEY_LENGTH
        self.client.api_key = secured_api_key
        res = self.index.search('')
        self.assertEqual(res['nbHits'], 5)
        self.client.api_key = old_key

    def test_search_with_long_secured_api_key(self):
        old_key = self.client.api_key

        tags = set('x{0}'.format(100000 + i) for i in range(1000))
        secured_api_key = self.client.generate_secured_api_key(
            os.environ['ALGOLIA_API_KEY_SEARCH'],
            dict(filters=' OR '.join(tags)),
        )
        assert len(secured_api_key) > MAX_API_KEY_LENGTH
        self.client.api_key = secured_api_key
        res = self.index.search('')
        self.assertEqual(res['nbHits'], 0)
        self.client.api_key = old_key


class IndexWithModifiableDataTest(IndexTest):
    """Tests that use one index with initial data and modify it."""

    def setUp(self):
        self.objs = self.factory.fake_contact(5)
        task = self.index.add_objects(self.objs)
        self.index.wait_task(task['taskID'])
        self.objectIDs = task['objectIDs']

    def tearDown(self):
        self.index.clear_index()

    def test_delete_object(self):
        task = self.index.delete_object(self.objectIDs[2])
        self.index.wait_task(task['taskID'])

        params = {'attributesToRetrieve': ['objectID']}
        res_ids = [obj['objectID'] for obj in self.index.browse_all(params)]
        self.assertEqual(len(res_ids), 4)
        self.assertNotIn(self.objectIDs[2], res_ids)
        for elt in res_ids:
            self.assertIn(elt, self.objectIDs)

    def test_delete_objects(self):
        task = self.index.delete_objects(self.objectIDs[0:3])
        self.index.wait_task(task['taskID'])

        params = {'attributesToRetrieve': ['objectID']}
        res_ids = [obj['objectID'] for obj in self.index.browse_all(params)]
        self.assertEqual(len(res_ids), 2)
        for i in range(3):
            self.assertNotIn(self.objectIDs[0], res_ids)
        for elt in res_ids:
            self.assertIn(elt, self.objectIDs)

    def test_delete_by_query(self):
        task = self.index.delete_by_query(self.objs[2]['name'][0])
        self.index.wait_task(task['taskID'])

        res = self.index.search('', {'hitsPerPage': 0})
        self.assertTrue(res['nbHits'] < 5)

    def test_batch(self):
        requests = [
            {
                'action': 'addObject',
                'body': self.factory.fake_contact()
            }, {
                'action': 'addObject',
                'body': self.factory.fake_contact()
            }
        ]

        task = self.index.batch({'requests': requests})
        self.index.wait_task(task['taskID'])
        res = self.index.search('', {'hitsPerPage': 0})
        self.assertEqual(res['nbHits'], 7)

        body_update = dict(self.objs[2])
        body_update['name'] = 'Jòseph Diã'
        requests = [
            {
                'action': 'updateObject',
                'body': body_update,
                'objectID': self.objectIDs[2]
            }, {
                'action': 'deleteObject',
                'objectID': self.objectIDs[0]
            }
        ]

        task = self.index.batch(requests)
        self.index.wait_task(task['taskID'])
        res = self.index.get_object(self.objectIDs[2])
        self.assertDictContainsSubset(body_update, res)

        with self.assertRaisesRegexp(AlgoliaException, 'does not exist'):
            self.index.get_object(self.objectIDs[0])
