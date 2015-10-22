# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from random import randint

try:
    import unittest2 as unittest  # py26
except ImportError:
    import unittest

from algoliasearch.client import Client

from .helpers import safe_index_name
from .helpers import get_api_client
from .helpers import FakeData


class ClientTest(unittest.TestCase):
    """Abstract class for all client tests."""

    @classmethod
    def setUpClass(cls):
        cls.client = get_api_client()
        cls.index_name = [
            safe_index_name('àlgol?à1-python{0}'.format(randint(1, 1000))),
            safe_index_name('àlgol?à2-python{0}'.format(randint(1, 1000))),
        ]
        cls.index = [cls.client.init_index(name) for name in cls.index_name]
        for name in cls.index_name:
            cls.client.delete_index(name)

        cls.factory = FakeData()

    @classmethod
    def tearDownClass(cls):
        for name in cls.index_name:
            cls.client.delete_index(name)


class ClientNoDataOperationsTest(ClientTest):
    """Tests that use two index and don't make any data operations."""

    def test_rate_limit_forward(self):
        hearders_rate_limit = {
            'X-Forwarded-For': '127.0.0.1',
            'X-Forwarded-API-Key': 'userSearchKey'
        }

        self.client.enable_rate_limit_forward('127.0.0.1', 'userSearchKey')
        self.assertDictContainsSubset(hearders_rate_limit, self.client.headers)

        self.client.disable_rate_limit_forward()
        for key in hearders_rate_limit.keys():
            self.assertNotIn(key, self.client.headers)

    def test_set_end_user_ip(self):
        self.client.set_end_user_ip('192.168.0.1')
        self.assertIn('X-Forwarded-For', self.client.headers)
        self.assertEqual(self.client.headers['X-Forwarded-For'], '192.168.0.1')

    def test_set_extra_headers(self):
        self.client.set_extra_headers(Private=True)
        self.assertIn('Private', self.client.headers)
        self.assertEqual(self.client.headers['Private'], True)

        self.client.set_extra_headers(**{
            'X-User': 223254,
            'X-Privacy-Settings': 'NSA-Free'
        })
        self.assertIn('X-User', self.client.headers)
        self.assertEqual(self.client.headers['X-User'], 223254)
        self.assertIn('X-Privacy-Settings', self.client.headers)
        self.assertEqual(self.client.headers['X-Privacy-Settings'], 'NSA-Free')

    def test_get_logs(self):
        res = self.client.get_logs(length=1)
        self.assertEqual(len(res['logs']), 1)

        res = self.client.get_logs(length=3)
        self.assertEqual(len(res['logs']), 3)

    def test_change_api_key(self):
        client = get_api_client()
        client.api_key = 'your_api_key'
        self.assertEqual(client._api_key, 'your_api_key')
        self.assertEqual(client.headers['X-Algolia-API-Key'], 'your_api_key')

    def test_subclassing_client(self):
        class SubClient(Client):
            def __init__(self, user_name, *args, **kwargs):
                super(SubClient, self).__init__(*args, **kwargs)
                self._user_name = user_name
                self.set_extra_headers(**{'X-User': user_name})

            @property
            def user_name(self):
                return self._user_name

        sub_client = SubClient('algolia', 'myAppID', 'myApiKey')
        self.assertEqual(sub_client.app_id, 'myAppID')
        self.assertEqual(sub_client.api_key, 'myApiKey')
        self.assertEqual(sub_client.user_name, 'algolia')
        self.assertIn('X-User', sub_client.headers)
        self.assertEqual(sub_client.headers['X-User'], 'algolia')


class ClientWithDataTest(ClientTest):
    """Tests that use two index with initial data."""

    def setUp(self):
        self.objs = [
            self.factory.fake_contact(5),
            self.factory.fake_contact(5)
        ]
        task = [self.index[i].add_objects(self.objs[i]) for i in range(2)]
        self.objectsIDs = []
        for i, t in enumerate(task):
            self.index[i].wait_task(t['taskID'])
            self.objectsIDs.append(t['objectIDs'])

    def tearDown(self):
        for index in self.index:
            index.clear_index()

    def test_list_indexes(self):
        res = self.client.list_indexes()
        res_names = [elt['name'] for elt in res['items']]
        for name in self.index_name:
            self.assertIn(name, res_names)

    def test_clear_index(self):
        task = self.index[0].clear_index()
        self.index[0].wait_task(task['taskID'])
        res = self.index[0].search('')
        self.assertEqual(res['nbHits'], 0)

        res = self.index[1].search('', {'hitsPerPage': 0})
        self.assertEqual(res['nbHits'], 5)

    def test_copy(self):
        task = self.client.copy_index(self.index_name[0], self.index_name[1])
        self.index[0].wait_task(task['taskID'])

        res = self.client.list_indexes()
        res_names = [elt['name'] for elt in res['items']]
        for name in self.index_name:
            self.assertIn(name, res_names)

        res = [index.search('') for index in self.index]
        self.assertListEqual(res[0]['hits'], res[1]['hits'])

    def test_move(self):
        task = self.client.move_index(self.index_name[0], self.index_name[1])
        self.index[0].wait_task(task['taskID'])

        res = self.client.list_indexes()
        res_names = [elt['name'] for elt in res['items']]
        self.assertNotIn(self.index_name[0], res_names)
        self.assertIn(self.index_name[1], res_names)

        res = self.index[1].search('', {'attributesToRetrieve': ['objectID']})
        res_ids = [elt['objectID'] for elt in res['hits']]
        for elt in res_ids:
            self.assertIn(elt, self.objectsIDs[0])
            self.assertNotIn(elt, self.objectsIDs[1])

    def test_delete_index(self):
        task = self.client.delete_index(self.index_name[0])
        self.index[0].wait_task(task['taskID'])

        res = self.client.list_indexes()
        res_names = [elt['name'] for elt in res['items']]
        self.assertNotIn(self.index_name[0], res_names)
        self.assertIn(self.index_name[1], res_names)

    def test_batch_multiple_indexes(self):
        params = {'hitsPerPage': 0}
        requests = [
            {
                'action': 'addObject',
                'indexName': self.index_name[0],
                'body': self.factory.fake_contact()
            }, {
                'action': 'addObject',
                'indexName': self.index_name[1],
                'body': self.factory.fake_contact()
            }, {
                'action': 'addObject',
                'indexName': self.index_name[0],
                'body': self.factory.fake_contact()
            }
        ]

        task = self.client.batch({'requests': requests})
        for i, name in enumerate(self.index_name):
            self.index[i].wait_task(task['taskID'][name])

        res = self.index[0].search('', params)
        self.assertEqual(res['nbHits'], 7)
        res = self.index[1].search('', params)
        self.assertEqual(res['nbHits'], 6)

        requests = [
            {
                'action': 'deleteObject',
                'indexName': self.index_name[0],
                'objectID': self.objectsIDs[0][2]
            }, {
                'action': 'deleteObject',
                'indexName': self.index_name[1],
                'objectID': self.objectsIDs[1][1]
            }, {
                'action': 'deleteObject',
                'indexName': self.index_name[1],
                'objectID': self.objectsIDs[1][0]
            }, {
                'action': 'deleteObject',
                'indexName': self.index_name[0],
                'objectID': self.objectsIDs[0][3]
            }, {
                'action': 'deleteObject',
                'indexName': self.index_name[1],
                'objectID': self.objectsIDs[1][2]
            }
        ]

        task = self.client.batch(requests)
        for i, name in enumerate(self.index_name):
            self.index[i].wait_task(task['taskID'][name])

        res = self.index[0].search('', params)
        self.assertEqual(res['nbHits'], 5)
        res = self.index[1].search('', params)
        self.assertEqual(res['nbHits'], 3)

    def test_multiple_queries(self):
        res = self.client.multiple_queries([
            {'indexName': self.index_name[0], 'query': ''},
            {'indexName': self.index_name[1], 'query': ''}
        ])

        self.assertEqual(len(res['results']), 2)
        for i, res in enumerate(res['results']):
            res_ids = [elt['objectID'] for elt in res['hits']]
            for elt in self.objectsIDs[i]:
                self.assertIn(elt, res_ids)
