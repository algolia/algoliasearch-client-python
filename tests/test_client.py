# -*- coding: utf-8 -*-

import unittest
import os
import time
import hashlib
import hmac
from decimal import *

from algoliasearch import algoliasearch


def safe_index_name(name):
    if 'TRAVIS' not in os.environ:
        return name
    job = os.environ['TRAVIS_JOB_NUMBER']
    return '%s_travis-%s' % (name, job)


class ClientTest(unittest.TestCase):
    def setUp(self):
        try:
            self.name = unichr(224) + 'lgol?' + unichr(224) + '-python'
            self.name2 = unichr(224) + 'lgol?' + unichr(224) + '2-python'
            self.name_obj = unichr(224) + '/go/?' + unichr(224) + '2-python'
        except Exception:
            self.name = 'àlgol?à-python'
            self.name2 = 'àlgol?à2-python'
            self.name_obj = 'à/go/?à2-python'

        self.client = algoliasearch.Client(
            os.environ['ALGOLIA_APPLICATION_ID'],
            os.environ['ALGOLIA_API_KEY'])
        index_name = safe_index_name(self.name)
        try:
            self.client.delete_index(index_name)
        except algoliasearch.AlgoliaException:
            pass
        self.index = self.client.init_index(index_name)

    def tearDown(self):
        index_name = safe_index_name(self.name)
        try:
            self.client.delete_index(index_name)
        except algoliasearch.AlgoliaException:
            pass
        index_name2 = safe_index_name(self.name2)
        try:
            self.client.delete_index(index_name2)
        except algoliasearch.AlgoliaException:
            pass

    def test_deleteByQuery(self):
        task = self.index.batch([ \
        {'action': 'addObject', 'body': {'name': 'San Francisco', 'objectID': '40'}}   \
      , {'action': 'addObject', 'body': {'name': 'San Francisco', 'objectID': '41'}}   \
      , {'action': 'addObject', 'body': {'name': 'Los Angeles', 'objectID': '42'}}                          \
      ])
        self.index.wait_task(task['taskID'])

        task = self.index.delete_by_query('San Francisco')
        self.index.wait_task(task['taskID'])

        res = self.index.search('')
        self.assertEquals(len(res['hits']), 1)

    def test_user_key(self):
        task = self.index.add_object({'name': 'Paris'}, self.name_obj)
        self.index.wait_task(task['taskID'])
        res = self.index.list_user_keys()
        new_key = self.index.add_user_key(['search'])
        time.sleep(5)
        self.assertTrue(new_key['key'] != '')
        res_after = self.index.list_user_keys()
        contains = False
        for it in res_after['keys']:
            contains = contains or it['value'] == new_key['key']
        self.assertTrue(contains)
        key = self.index.get_user_key_acl(new_key['key'])
        self.assertEquals(key['acl'][0], 'search')
        new_key = self.index.update_user_key(new_key['key'], ['addObject'])
        time.sleep(5)
        key = self.index.get_user_key_acl(new_key['key'])
        self.assertEquals(key['acl'][0], 'addObject')
        task = self.index.delete_user_key(new_key['key'])
        time.sleep(5)
        res_end = self.index.list_user_keys()
        contains = False
        for it in res_end['keys']:
            contains = contains or it['value'] == new_key['key']
        self.assertTrue(not contains)

        res = self.client.list_user_keys()
        new_key = self.client.add_user_key(['search'])
        time.sleep(5)
        self.assertTrue(new_key['key'] != '')
        res_after = self.client.list_user_keys()
        contains = False
        for it in res_after['keys']:
            contains = contains or it['value'] == new_key['key']
        self.assertTrue(contains)
        key = self.client.get_user_key_acl(new_key['key'])
        self.assertEquals(key['acl'][0], 'search')
        new_key = self.client.update_user_key(new_key['key'], ['addObject'])
        time.sleep(5)
        key = self.client.get_user_key_acl(new_key['key'])
        self.assertEquals(key['acl'][0], 'addObject')
        task = self.client.delete_user_key(new_key['key'])
        time.sleep(5)
        res_end = self.client.list_user_keys()
        contains = False
        for it in res_end['keys']:
            contains = contains or it['value'] == new_key['key']
        self.assertTrue(not contains)

    def test_settings(self):
        task = self.index.set_settings({'attributesToRetrieve': ['name']})
        self.index.wait_task(task['taskID'])
        settings = self.index.get_settings()
        self.assertEquals(len(settings['attributesToRetrieve']), 1)
        self.assertEquals(settings['attributesToRetrieve'][0], 'name')

    def test_URLEncode(self):
        task = self.index.save_object(
            {'name': 'San Francisco',
             'objectID': self.name_obj})
        self.index.wait_task(task['taskID'])

        obj = self.index.get_object(self.name_obj, 'name')
        self.assertEquals(obj['name'], 'San Francisco')

        task = self.index.partial_update_object(
            {'name': 'San Diego',
             'objectID': self.name_obj})
        self.index.wait_task(task['taskID'])
        obj = self.index.get_object(self.name_obj)
        self.assertEquals(obj['name'], 'San Diego')

        task = self.index.save_objects(
            [{'name': 'Los Angeles',
              'objectID': self.name_obj}])
        self.index.wait_task(task['taskID'])

        obj = self.index.get_object(self.name_obj)
        self.assertEquals(obj['name'], 'Los Angeles')

    def test_secured_keys(self):
        self.assertEquals(
            '1fd74b206c64fb49fdcd7a5f3004356cd3bdc9d9aba8733656443e64daafc417',
            hmac.new('my_api_key'.encode('utf-8'), '(public,user1)'.encode(
                'utf-8'), hashlib.sha256).hexdigest())
        key = self.client.generate_secured_api_key('my_api_key',
                                                   '(public,user1)')
        self.assertEquals(key, hmac.new('my_api_key'.encode('utf-8'),
                                        '(public,user1)'.encode('utf-8'),
                                        hashlib.sha256).hexdigest())
        key = self.client.generate_secured_api_key('my_api_key',
                                                   '(public,user1)', 42)
        self.assertEquals(key, hmac.new('my_api_key'.encode('utf-8'),
                                        '(public,user1)42'.encode('utf-8'),
                                        hashlib.sha256).hexdigest())
        key = self.client.generate_secured_api_key('my_api_key', ['public'])
        self.assertEquals(key, hmac.new('my_api_key'.encode(
            'utf-8'), 'public'.encode('utf-8'), hashlib.sha256).hexdigest())
        key = self.client.generate_secured_api_key(
            'my_api_key', ['public', ['premium', 'vip']])
        self.assertEquals(key, hmac.new('my_api_key'.encode('utf-8'),
                                        'public,(premium,vip)'.encode('utf-8'),
                                        hashlib.sha256).hexdigest())

    def test_multipleQueries(self):
        task = self.index.add_object({'name': 'Paris'}, self.name_obj)
        self.index.wait_task(task['taskID'])
        results = self.client.multiple_queries(
            [{'indexName': safe_index_name(self.name),
              'query': ''}])
        self.assertEquals(len(results['results']), 1)
        self.assertEquals(len(results['results'][0]['hits']), 1)
        self.assertEquals('Paris', results['results'][0]['hits'][0]['name'])

    def test_decimal(self):
        value = Decimal('3.14')
        task = self.index.save_object({
            'value': value,
            'objectID': self.name_obj
        })
        self.index.wait_task(task['taskID'])

        obj = self.index.get_object(self.name_obj)
        self.assertEquals(obj['value'], float(value))

    def test_float(self):
        value = float('3.14')
        task = self.index.save_object(
            {'value': value,
             'objectID': self.name_obj})
        self.index.wait_task(task['taskID'])

        obj = self.index.get_object(self.name_obj)
        self.assertEquals(obj['value'], value)

    def test_disjunctive_faceting(self):
        self.index.set_settings(
            {'attributesForFacetting': ['city', 'stars', 'facilities']})
        task = self.index.add_objects([{
            'name': 'Hotel A',
            'stars': '*',
            'facilities': ['wifi', 'bath', 'spa'],
            'city': 'Paris'
        }, {
            'name': 'Hotel B',
            'stars': '*',
            'facilities': ['wifi'],
            'city': 'Paris'
        }, {
            'name': 'Hotel C',
            'stars': '**',
            'facilities': ['bath'],
            'city': 'San Francisco'
        }, {
            'name': 'Hotel D',
            'stars': '****',
            'facilities': ['spa'],
            'city': 'Paris'
        }, {
            'name': 'Hotel E',
            'stars': '****',
            'facilities': ['spa'],
            'city': 'New York'
        }, ])
        self.index.wait_task(task['taskID'])

        answer = self.index.search_disjunctive_faceting(
            'h', ['stars', 'facilities'], {'facets': 'city'})
        self.assertEquals(answer['nbHits'], 5)
        self.assertEquals(len(answer['facets']), 1)
        self.assertEquals(len(answer['disjunctiveFacets']), 2)

        answer = self.index.search_disjunctive_faceting('h', [
            'stars', 'facilities'
        ], {'facets': 'city'}, {'stars': ['*']})
        self.assertEquals(answer['nbHits'], 2)
        self.assertEquals(len(answer['facets']), 1)
        self.assertEquals(len(answer['disjunctiveFacets']), 2)
        self.assertEquals(answer['disjunctiveFacets']['stars']['*'], 2)
        self.assertEquals(answer['disjunctiveFacets']['stars']['**'], 1)
        self.assertEquals(answer['disjunctiveFacets']['stars']['****'], 2)

        answer = self.index.search_disjunctive_faceting('h', [
            'stars', 'facilities'
        ], {'facets': 'city'}, {'stars': ['*'],
                                'city': ['Paris']})
        self.assertEquals(answer['nbHits'], 2)
        self.assertEquals(len(answer['facets']), 1)
        self.assertEquals(len(answer['disjunctiveFacets']), 2)
        self.assertEquals(answer['disjunctiveFacets']['stars']['*'], 2)
        self.assertEquals(answer['disjunctiveFacets']['stars']['****'], 1)

        answer = self.index.search_disjunctive_faceting('h', [
            'stars', 'facilities'
        ], {'facets': 'city'}, {'stars': ['*', '****'],
                                'city': ['Paris']})
        self.assertEquals(answer['nbHits'], 3)
        self.assertEquals(len(answer['facets']), 1)
        self.assertEquals(len(answer['disjunctiveFacets']), 2)
        self.assertEquals(answer['disjunctiveFacets']['stars']['*'], 2)
        self.assertEquals(answer['disjunctiveFacets']['stars']['****'], 1)

    def test_encodeBoolean(self):
        task = self.index.add_object({'score': 3525}, self.name_obj)
        self.index.wait_task(task['taskID'])
        results = self.index.search('353',
                                    {'allowTyposOnNumericTokens': False})
        self.assertEquals(len(results['hits']), 0)

    def test_attributeToRetrieve(self):
        task = self.index.add_object({'name': 'Paris',
                                      'short_name': 'Pa'}, self.name_obj)
        self.index.wait_task(task['taskID'])
        results = self.index.search(
            '', {'attributesToRetrieve': ['name', 'short_name']})
        self.assertEquals(len(results['hits']), 1)
        self.assertEquals('Paris', results['hits'][0]['name'])
        self.assertEquals('Pa', results['hits'][0]['short_name'])

        results = self.index.search(
            '', {'attributesToRetrieve': 'name,short_name'})
        self.assertEquals(len(results['hits']), 1)
        self.assertEquals('Paris', results['hits'][0]['name'])
        self.assertEquals('Pa', results['hits'][0]['short_name'])

    def test_batch_multiple_indexes(self):
        task = self.client.batch([{'action': 'addObject', 'indexName': self.index.index_name, 'body': {'name': 'San Francisco'}}   \
      , {'action': 'addObject', 'indexName': self.index.index_name, 'body': {'name': 'Los Angeles'}}                          \
      , {'action': 'updateObject', 'indexName': self.index.index_name, 'body': {'name': 'San Diego'}, 'objectID': '42'}    \
      , {'action': 'updateObject', 'indexName': self.index.index_name, 'body': {'name': 'Los Gatos'}, 'objectID': self.name_obj}    \
      ])
        self.index.wait_task(task['taskID'][self.index.index_name])
        obj = self.index.get_object('42')
        self.assertEquals(obj['name'], 'San Diego')

        res = self.index.search('')
        self.assertEquals(len(res['hits']), 4)
