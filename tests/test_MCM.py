# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from random import randint
import time
import os

try:
    import unittest2 as unittest  # py26
except ImportError:
    import unittest

from algoliasearch.client import Client, MAX_API_KEY_LENGTH, RequestOptions
from algoliasearch.helpers import AlgoliaException,PY2

from .helpers import safe_index_name
from .helpers import get_api_client
from .helpers import FakeData, FakeSession


class MCMTest(unittest.TestCase):
    """Abstract class for all client tests."""

    def uniq_user_id(self, name):
        if 'TRAVIS' not in os.environ:
            return name
        job = os.environ['TRAVIS_JOB_NUMBER']
        return '{0}-travis-{1}'.format(name, job)

    @classmethod
    def setUpClass(cls):
        unittest.TestLoader().sortTestMethodsUsing = None
        if 'APPENGINE_RUNTIME' in os.environ:
            from google.appengine.api import apiproxy_stub_map 
            from google.appengine.api import urlfetch_stub
            apiproxy_stub_map.apiproxy = apiproxy_stub_map.APIProxyStubMap()
            apiproxy_stub_map.apiproxy.RegisterStub('urlfetch',  urlfetch_stub.URLFetchServiceStub())
        cls.client = Client(os.environ['ALGOLIA_APPLICATION_ID_MCM'],
                  os.environ['ALGOLIA_API_KEY_MCM'])
        if PY2:
            cls.strType = unicode
        else:
            cls.strType = str

    def test_1_list_clusters(self):
        answer = self.client.list_clusters()

        self.assertTrue(isinstance(answer, dict))
        self.assertTrue(isinstance(answer['clusters'], list))
        self.assertTrue(len(answer['clusters']) > 0)
        self.assertTrue(isinstance(answer['clusters'][0]['clusterName'], self.strType))
        self.assertTrue(isinstance(answer['clusters'][0]['nbRecords'], int))
        self.assertTrue(isinstance(answer['clusters'][0]['nbUserIDs'], int))
        self.assertTrue(isinstance(answer['clusters'][0]['dataSize'], int))

    def test_2_assign_user_id(self):
        clusterName = self.client.list_clusters()['clusters'][0]['clusterName']
        answer = self.client.assign_user_id(self.uniq_user_id('python-client'), clusterName)

        self.assertTrue(isinstance(answer, dict))
        self.assertTrue(isinstance(answer['createdAt'], self.strType))
        time.sleep(2) # Sleep to let the cluster publish the change

    def test_3_list_user_ids(self):
        answer = self.client.list_user_ids()


        self.assertTrue(isinstance(answer, dict))
        self.assertTrue(isinstance(answer['userIDs'], list))
        self.assertTrue(len(answer['userIDs']) > 0)
        self.assertTrue(isinstance(answer['userIDs'][0]['userID'], self.strType))
        self.assertTrue(isinstance(answer['userIDs'][0]['clusterName'], self.strType))
        self.assertTrue(isinstance(answer['userIDs'][0]['nbRecords'], int))
        self.assertTrue(isinstance(answer['userIDs'][0]['dataSize'], int))

    def test_4_get_top_user_id(self):
        clusterName = self.client.list_clusters()['clusters'][0]['clusterName']
        answer = self.client.get_top_user_id()

        self.assertTrue(isinstance(answer, dict))
        self.assertTrue(isinstance(answer['topUsers'], dict))
        self.assertTrue(len(answer['topUsers']) > 0)
        self.assertTrue(isinstance(answer['topUsers'][clusterName], list))
        self.assertTrue(isinstance(answer['topUsers'][clusterName][0]['userID'], self.strType))
        self.assertTrue(isinstance(answer['topUsers'][clusterName][0]['nbRecords'], int))
        self.assertTrue(isinstance(answer['topUsers'][clusterName][0]['dataSize'], int))

    def test_5_get_user_id(self):
        answer = self.client.get_user_id(self.uniq_user_id('python-client'))

        self.assertTrue(isinstance(answer, dict))
        self.assertTrue(isinstance(answer['userID'], self.strType))
        self.assertTrue(isinstance(answer['clusterName'], self.strType))
        self.assertTrue(isinstance(answer['nbRecords'], int))
        self.assertTrue(isinstance(answer['dataSize'], int))

    def test_6_search_user_ids(self):
        clusterName = self.client.list_clusters()['clusters'][0]['clusterName']
        answer = self.client.search_user_ids(self.uniq_user_id('python-client'), clusterName, 0, 1000)


        self.assertTrue(isinstance(answer, dict))
        self.assertTrue(isinstance(answer['nbHits'], int))
        self.assertTrue(isinstance(answer['page'], int))
        self.assertTrue(isinstance(answer['hitsPerPage'], int))
        self.assertTrue(isinstance(answer['hits'], list))
        self.assertTrue(len(answer['hits']) > 0)
        self.assertTrue(isinstance(answer['hits'][0]['userID'], self.strType))
        self.assertTrue(isinstance(answer['hits'][0]['clusterName'], self.strType))
        self.assertTrue(isinstance(answer['hits'][0]['nbRecords'], int))
        self.assertTrue(isinstance(answer['hits'][0]['dataSize'], int))

    def test_7_remove_user_id(self):
        answer = self.client.remove_user_id(self.uniq_user_id('python-client'))

        print(answer)
        self.assertTrue(isinstance(answer, dict))
        self.assertTrue(isinstance(answer['deletedAt'], self.strType))




