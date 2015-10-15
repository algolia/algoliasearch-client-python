# -*- coding: utf-8 -*-

import unittest
import os
import time
import hashlib
import hmac
import sys

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

    def test_network(self):
        batch = []
        for i in range(1, 1000):
            batch.append({'action': 'addObject', 'body': {
                'test1': 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                'test2': 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                'test3': 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
            }})
        self.index.batch(batch)

    def test_new_secured_keys(self):
        self.assertEquals("MDZkNWNjNDY4M2MzMDA0NmUyNmNkZjY5OTMzYjVlNmVlMTk1NTEwMGNmNTVjZmJhMmIwOTIzYjdjMTk2NTFiMnRhZ0ZpbHRlcnM9JTI4cHVibGljJTJDdXNlcjElMjk=", self.client.generate_secured_api_key("182634d8894831d5dbce3b3185c50881", "(public,user1)"));
        self.assertEquals("MDZkNWNjNDY4M2MzMDA0NmUyNmNkZjY5OTMzYjVlNmVlMTk1NTEwMGNmNTVjZmJhMmIwOTIzYjdjMTk2NTFiMnRhZ0ZpbHRlcnM9JTI4cHVibGljJTJDdXNlcjElMjk=", self.client.generate_secured_api_key("182634d8894831d5dbce3b3185c50881", {'tagFilters': "(public,user1)"}));
        if sys.version_info[0] == 2:
            self.assertEquals("ZDU0N2YzZjA3NGZkZGM2OTUxNzY3NzhkZDI3YWFkMjhhNzU5OTBiOGIyYTgyYzFmMjFjZTY4NTA0ODNiN2I1ZnVzZXJUb2tlbj00MiZ0YWdGaWx0ZXJzPSUyOHB1YmxpYyUyQ3VzZXIxJTI5", self.client.generate_secured_api_key("182634d8894831d5dbce3b3185c50881", {'tagFilters': "(public,user1)", 'userToken': '42'}));
            self.assertEquals("ZDU0N2YzZjA3NGZkZGM2OTUxNzY3NzhkZDI3YWFkMjhhNzU5OTBiOGIyYTgyYzFmMjFjZTY4NTA0ODNiN2I1ZnVzZXJUb2tlbj00MiZ0YWdGaWx0ZXJzPSUyOHB1YmxpYyUyQ3VzZXIxJTI5", self.client.generate_secured_api_key("182634d8894831d5dbce3b3185c50881", {'tagFilters': "(public,user1)"}, '42'));
        else:
            self.assertEquals("OGYwN2NlNTdlOGM2ZmM4MjA5NGM0ZmYwNTk3MDBkNzMzZjQ0MDI3MWZjNTNjM2Y3YTAzMWM4NTBkMzRiNTM5YnRhZ0ZpbHRlcnM9JTI4cHVibGljJTJDdXNlcjElMjkmdXNlclRva2VuPTQy", self.client.generate_secured_api_key("182634d8894831d5dbce3b3185c50881", {'tagFilters': "(public,user1)", 'userToken': '42'}));
            self.assertEquals("OGYwN2NlNTdlOGM2ZmM4MjA5NGM0ZmYwNTk3MDBkNzMzZjQ0MDI3MWZjNTNjM2Y3YTAzMWM4NTBkMzRiNTM5YnRhZ0ZpbHRlcnM9JTI4cHVibGljJTJDdXNlcjElMjkmdXNlclRva2VuPTQy", self.client.generate_secured_api_key("182634d8894831d5dbce3b3185c50881", {'tagFilters': "(public,user1)"}, '42'));


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
