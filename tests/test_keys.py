# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import time
import hmac
import hashlib
from random import randint

try:
    import unittest2 as unittest  # py26
except ImportError:
    import unittest

from .helpers import safe_index_name
from .helpers import get_api_client
from .helpers import FakeData


class KeyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = get_api_client()
        cls.index_name = safe_index_name('àlgol?à-python{0}'.format(
                                         randint(1, 1000)))
        cls.index = cls.client.init_index(cls.index_name)
        cls.client.delete_index(cls.index_name)

        cls.factory = FakeData()

    def setUp(self):
        task = self.index.add_objects(self.factory.fake_contact(5))
        self.index.wait_task(task['taskID'])

    def tearDown(self):
        self.client.delete_index(self.index_name)

    def test_list_user_keys(self):
        res = self.client.list_user_keys()
        self.assertIn('keys', res)

    def test_add_user_keys(self):
        keys = []

        res = self.client.add_user_key(['search'])
        self.assertGreater(len(res['key']), 1)
        keys.append(res['key'])

        res = self.client.add_user_key(['search'],
                                       max_queries_per_ip_per_hour=10)
        self.assertGreater(len(res['key']), 1)
        keys.append(res['key'])

        res = self.client.add_user_key(['search'], max_hits_per_query=5)
        self.assertGreater(len(res['key']), 1)
        keys.append(res['key'])

        res = self.client.add_user_key(['search'], validity=30)
        self.assertGreater(len(res['key']), 1)

        for key in keys:
            self.client.delete_user_key(key)

    def test_get_user_key(self):
        res = self.client.add_user_key(['search'])
        key = res['key']
        time.sleep(5)

        res = self.client.get_user_key_acl(key)
        self.assertEqual(res['value'], key)
        self.assertSetEqual(set(res['acl']), set(['search']))

        self.client.delete_user_key(key)

    def test_update_user_keys(self):
        keys = []

        for i in range(3):
            res = self.client.add_user_key(['search'])
            keys.append(res['key'])

        time.sleep(5)

        res = self.client.update_user_key(keys[0], ['addObject'],
                                          max_queries_per_ip_per_hour=5)
        self.assertGreater(len(res['key']), 0)
        time.sleep(5)
        res = self.client.get_user_key_acl(keys[0])
        self.assertSetEqual(set(res['acl']), set(['addObject']))
        self.assertEqual(res['maxQueriesPerIPPerHour'], 5)

        res = self.client.update_user_key(keys[1], ['deleteObject'],
                                          max_hits_per_query=10)
        self.assertGreater(len(res['key']), 0)
        time.sleep(5)
        res = self.client.get_user_key_acl(keys[1])
        self.assertSetEqual(set(res['acl']), set(['deleteObject']))
        self.assertEqual(res['maxHitsPerQuery'], 10)

        res = self.client.update_user_key(keys[2], ['settings', 'search'],
                                          validity=60)
        self.assertGreater(len(res['key']), 0)
        time.sleep(5)
        res = self.client.get_user_key_acl(keys[2])
        self.assertSetEqual(set(res['acl']), set(['settings', 'search']))
        self.assertIn('validity', res)
        self.assertGreater(res['validity'], 0)

        for key in keys:
            self.client.delete_user_key(key)

    def test_delete_user_keys(self):
        res = self.client.add_user_key(['search'])
        key = res['key']
        time.sleep(5)

        self.client.delete_user_key(key)
        time.sleep(5)

        res = self.client.list_user_keys()
        res_keys = [elt['value'] for elt in res['keys']]
        self.assertNotIn(key, res_keys)

    def test_index_list_user_keys(self):
        res = self.index.list_user_keys()
        self.assertIn('keys', res)

    def test_index_add_user_keys(self):
        keys = []

        res = self.index.add_user_key(['search'])
        self.assertGreater(len(res['key']), 1)
        keys.append(res['key'])

        res = self.index.add_user_key(['search'],
                                      max_queries_per_ip_per_hour=10)
        self.assertGreater(len(res['key']), 1)
        keys.append(res['key'])

        res = self.index.add_user_key(['search'], max_hits_per_query=5)
        self.assertGreater(len(res['key']), 1)
        keys.append(res['key'])

        res = self.index.add_user_key(['search'], validity=30)
        self.assertGreater(len(res['key']), 1)

        for key in keys:
            self.index.delete_user_key(key)

    def test_index_get_user_key(self):
        res = self.index.add_user_key(['search'])
        key = res['key']
        time.sleep(5)

        res = self.index.get_user_key_acl(key)
        self.assertEqual(res['value'], key)
        self.assertSetEqual(set(res['acl']), set(['search']))

        self.index.delete_user_key(key)

    def test_index_update_user_keys(self):
        keys = []

        for i in range(3):
            res = self.index.add_user_key(['search'])
            keys.append(res['key'])

        time.sleep(5)

        res = self.index.update_user_key(keys[0], ['addObject'],
                                         max_queries_per_ip_per_hour=5)
        self.assertGreater(len(res['key']), 0)
        time.sleep(5)
        res = self.index.get_user_key_acl(keys[0])
        self.assertSetEqual(set(res['acl']), set(['addObject']))
        self.assertEqual(res['maxQueriesPerIPPerHour'], 5)

        res = self.index.update_user_key(keys[1], ['deleteObject'],
                                         max_hits_per_query=10)
        self.assertGreater(len(res['key']), 0)
        time.sleep(5)
        res = self.index.get_user_key_acl(keys[1])
        self.assertSetEqual(set(res['acl']), set(['deleteObject']))
        self.assertEqual(res['maxHitsPerQuery'], 10)

        res = self.index.update_user_key(keys[2], ['settings', 'search'],
                                         validity=60)
        self.assertGreater(len(res['key']), 0)
        time.sleep(5)
        res = self.index.get_user_key_acl(keys[2])
        self.assertSetEqual(set(res['acl']), set(['settings', 'search']))
        self.assertIn('validity', res)
        self.assertGreater(res['validity'], 0)

        for key in keys:
            self.index.delete_user_key(key)

    def test_index_delete_user_keys(self):
        res = self.index.add_user_key(['search'])
        key = res['key']
        time.sleep(5)

        self.index.delete_user_key(key)
        time.sleep(5)

        res = self.index.list_user_keys()
        res_keys = [elt['value'] for elt in res['keys']]
        self.assertNotIn(key, res_keys)
