import datetime
import os
import platform
import unittest

from algoliasearch.exceptions import RequestException
from algoliasearch.responses import MultipleResponse
from tests.helpers.factory import Factory as F


class TestSearchClient(unittest.TestCase):
    def setUp(self):
        self.client = F.client()
        self.index = F.index(self._testMethodName)

    def tearDown(self):
        self.index.delete()

    def test_copy_index(self):
        objects = [
            {'objectID': 'one', 'company': 'apple'},
            {'objectID': 'two', 'company': 'algolia'}
        ]

        responses = MultipleResponse([
            self.index.save_objects(objects),
            self.index.set_settings({'attributesForFaceting': ['company']}),
            self.index.save_synonym({
                'objectID': 'google_placeholder',
                'type': 'placeholder',
                'placeholder': '<GOOG>',
                'replacements': ['Google', 'GOOG']
            }),

            self.index.save_rule({
                "objectID": "company_auto_faceting",
                "condition": {
                    "anchoring": "contains",
                    "pattern": "{facet:company}",
                },
                "consequence": {
                    "params": {"automaticFacetFilters": ["company"]}
                }
            })
        ]).wait()

        responses.push(self.client.copy_settings(
            self.index.name, self.index.name + '_settings'
        ))

        responses.push(self.client.copy_rules(
            self.index.name, self.index.name + '_rules'
        ))

        responses.push(self.client.copy_synonyms(
            self.index.name, self.index.name + '_synonyms'
        ))

        responses.push(self.client.copy_index(
            self.index.name, self.index.name + '_full_copy'
        ))

        responses.wait()

        self.index.__SearchIndex_name = self.index.name + '_settings'
        self.assertEqual(
            self.index.get_settings()['attributesForFaceting'], ['company']
        )

        self.index.__SearchIndex_name = self.index.name + '_rules'
        self.index.get_rule('company_auto_faceting')

        self.index.__SearchIndex_name = self.index.name + '_synonym'
        self.index.get_synonym('google_placeholder')

        self.index.__SearchIndex_name = self.index.name + '_full_copy'
        self.index.get_synonym('google_placeholder')
        self.index.get_rule('company_auto_faceting')
        self.assertEqual(
            self.index.get_settings()['attributesForFaceting'], ['company']
        )
        for obj in self.index.browse_objects():
            self.assertIn(obj, objects)

    def test_mcm(self):
        mcm = F.mcm()

        clusters = mcm.list_clusters()['clusters']
        self.assertEqual(len(clusters), 2)

        date = datetime.datetime.now().strftime("%Y-%m-%d")

        if 'TRAVIS' in os.environ:
            instance = os.environ['TRAVIS_JOB_NUMBER']
        else:
            instance = 'unknown'

        python_version = platform.python_version().replace('.', '')[:2]

        user_id = 'python%s-%s-%s' % (python_version, date, instance)

        mcm.assign_user_id(user_id, clusters[0]['clusterName']).wait()

        self.assertEqual(
            mcm.search_user_ids(user_id)['hits'][0]['userID'],
            user_id
        )

        users = mcm.list_user_ids()
        self.assertIsInstance(users, dict)
        self.assertIsInstance(users['userIDs'], list)
        self.assertTrue(len(users['userIDs']) > 0)

        users = mcm.get_top_user_ids()
        self.assertIsInstance(users, dict)
        self.assertIsInstance(users['topUsers'], dict)
        self.assertTrue(len(users['topUsers']) > 0)

        mcm.remove_user_id(user_id).wait()
        users = mcm.list_user_ids()

        date = datetime.datetime.now().strftime("%Y-%m-%d")

        startswith = 'python%s' % python_version
        startswith_except = 'python%s-%s' % (python_version, date)

        for user in users['userIDs']:
            if user['userID'].startswith(startswith) \
                    and not user['userID'].startswith(startswith_except):
                mcm.remove_user_id(user['userID'])
