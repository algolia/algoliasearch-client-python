# -*- coding: utf-8 -*-

import unittest
import os
import time
import hashlib
import hmac

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

    def test_wrong_app_id(self):
        client = algoliasearch.Client("fakeappID", "blabla")
        try:
            client.listIndexes()
            self.assertTrue(False)
        except algoliasearch.AlgoliaException as e:
            pass

    def test_retry(self):
      try:
          client = algoliasearch.Client(os.environ['ALGOLIA_APPLICATION_ID'], os.environ['ALGOLIA_API_KEY'], ["fakeapp-1.algolia.io", "fakeapp-2.algolia.io", os.environ['ALGOLIA_APPLICATION_ID'] + ".algolia.io"])
          client.listIndexes
      except algoliasearch.AlgoliaException as e:
          self.assertTrue(false)


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
