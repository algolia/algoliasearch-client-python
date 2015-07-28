# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from random import randint

try:
    import unittest2 as unittest  # py26
except ImportError:
    import unittest

from .helpers import safe_index_name
from .helpers import get_api_client
from .helpers import FakeData


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
        obj['objectID'] = '4242'
        task = self.index.save_object(obj)
        self.index.wait_task(task['taskID'])

        res = self.index.get_object(obj['objectID'])
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


class IndexWithReadOnlyDataTest(IndexTest):
    """Tests that use one index with initial data (read only)."""

    @classmethod
    def setUpClass(cls):
        super(IndexWithReadOnlyDataTest, cls).setUpClass()

        cls.objs = cls.factory.fake_contact(5)
        task = cls.index.add_objects(cls.objs)
        cls.index.wait_task(task['taskID'])
        cls.objectIDs = task['objectIDs']

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

    def test_algolia_exception(self):
        pass


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

        params = {'query': '', 'attributesToRetrieve': ['objectID']}
        res_ids = [obj['objectID'] for obj in self.index.browse_all(params)]
        self.assertEqual(len(res_ids), 4)
        self.assertNotIn(self.objectIDs[2], res_ids)
        for elt in res_ids:
            self.assertIn(elt, self.objectIDs)

    def test_delete_objects(self):
        task = self.index.delete_objects(self.objectIDs[0:3])
        self.index.wait_task(task['taskID'])

        params = {'query': '', 'attributesToRetrieve': ['objectID']}
        res_ids = [obj['objectID'] for obj in self.index.browse_all(params)]
        self.assertEqual(len(res_ids), 2)
        self.assertNotIn(self.objectIDs[0], res_ids)
        self.assertNotIn(self.objectIDs[1], res_ids)
        self.assertNotIn(self.objectIDs[2], res_ids)
        for elt in res_ids:
            self.assertIn(elt, self.objectIDs)
