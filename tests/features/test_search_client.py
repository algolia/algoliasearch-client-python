import datetime
import os
import platform
import time
import unittest

from algoliasearch.configs import SearchConfig
from algoliasearch.exceptions import RequestException
from algoliasearch.http.hosts import HostsCollection, Host, CallType
from algoliasearch.http.serializer import QueryParametersSerializer
from algoliasearch.responses import MultipleResponse
from algoliasearch.search_client import SearchClient
from tests.helpers.env import Env
from tests.helpers.factory import Factory as F, Factory


class TestSearchClient(unittest.TestCase):
    def setUp(self):
        self.client = F.search_client()
        self.index = F.index(self._testMethodName)
        self.index2 = self.index3 = self.index4 = self.index5 = self.index5 = self.index6 = None  # noqa: E501

    def tearDown(self):
        self.index.delete()

        indices = [self.index2, self.index3, self.index4, self.index5,
                   self.index6]
        indices_used = (index for index in indices if index is not None)
        for index in indices_used:
            index.delete()

    def test_copy_move_index(self):
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

        self.index2 = F.index('{}_settings'.format(self._testMethodName))
        responses.push(self.client.copy_settings(
            self.index.name, self.index2.name
        ))

        self.index3 = F.index('{}_rules'.format(self._testMethodName))
        responses.push(self.client.copy_rules(
            self.index.name, self.index3.name
        ))

        self.index4 = F.index('{}_synonyms'.format(self._testMethodName))
        responses.push(self.client.copy_synonyms(
            self.index.name, self.index4.name
        ))

        self.index5 = F.index('{}_full_copy'.format(self._testMethodName))
        responses.push(self.client.copy_index(
            self.index.name, self.index5.name
        ))

        responses.wait()

        self.assertEqual(
            self.index2.get_settings()['attributesForFaceting'], ['company']
        )

        self.index3.get_rule('company_auto_faceting')
        with self.assertRaises(RequestException) as cm:
            self.index3.get_synonym('google_placeholder')

        self.index4.get_synonym('google_placeholder')
        with self.assertRaises(RequestException) as cm:
            self.index4.get_rule('company_auto_faceting')

        self.index5.get_synonym('google_placeholder')
        self.index5.get_rule('company_auto_faceting')
        self.assertEqual(
            self.index5.get_settings()['attributesForFaceting'], ['company']
        )
        for obj in self.index5.browse_objects():
            self.assertIn(obj, objects)

        self.index6 = F.index('{}_after_move'.format(self._testMethodName))
        self.client.move_index(
            self.index.name,
            self.index6.name
        ).wait()

        self.index6.get_synonym('google_placeholder')
        self.index6.get_rule('company_auto_faceting')
        self.assertEqual(
            self.index6.get_settings()['attributesForFaceting'], ['company']
        )
        for obj in self.index6.browse_objects():
            self.assertIn(obj, objects)

        with self.assertRaises(RequestException) as cm:
            self.client.init_index(self.index.name).search('')

        self.assertEqual(cm.exception.status_code, 404)

    @unittest.skipIf(Env.is_community(),
                     "Community can not test mcm operations")
    def test_mcm(self):
        mcm = F.mcm()

        clusters = mcm.list_clusters()['clusters']
        self.assertEqual(len(clusters), 2)

        date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

        if 'TRAVIS' in os.environ:
            instance = os.environ['TRAVIS_JOB_NUMBER']
        else:
            instance = 'unknown'

        python_version = platform.python_version().replace('.', '')[:2]

        python_version += os.environ.get('TEST_TYPE', '')

        user_id = 'python{}-{}-{}'.format(python_version, date, instance)

        mcm.assign_user_id(user_id, clusters[0]['clusterName'])

        result = None
        while result is None:
            try:
                result = mcm.get_user_id(user_id)
            except RequestException:
                pass

        users_ids = [user['userID'] for user in
                     mcm.search_user_ids(user_id)['hits']]

        self.assertIn(
            user_id,
            users_ids
        )

        users = mcm.list_user_ids()
        self.assertIsInstance(users, dict)
        self.assertIsInstance(users['userIDs'], list)
        self.assertTrue(len(users['userIDs']) > 0)

        users = mcm.get_top_user_ids()
        self.assertIsInstance(users, dict)
        self.assertIsInstance(users['topUsers'], dict)
        self.assertTrue(len(users['topUsers']) > 0)

        result = None
        while result is None:
            try:
                result = mcm.remove_user_id(user_id)
            except RequestException:
                pass

        users = mcm.list_user_ids()

        date = datetime.datetime.now().strftime("%Y-%m-%d")

        a = 'python{}'.format(python_version)
        b = '{}-{}'.format(a, date)

        for user in users['userIDs']:
            user_id = user['userID']

            if user_id.startswith(a) and not user_id.startswith(b):
                mcm.remove_user_id(user['userID'])

    def test_api_keys(self):
        response = self.client.add_api_key(['search'], {
            "description": "A description",
            "indexes": ["index"],
            "maxHitsPerQuery": 1000,
            "maxQueriesPerIPPerHour": 1000,
            "queryParameters": "typoTolerance=strict",
            "referers": ["referer"],
            "validity": 600
        })

        response.wait()

        api_key = self.client.get_api_key(response.raw_response['key'])
        self.assertEqual(api_key['value'],
                         response.raw_response['key'])

        api_keys = list(map(lambda facet: api_key['value'],
                            self.client.list_api_keys()['keys']))

        self.assertIn(api_key['value'], api_keys)

        self.client.update_api_key(api_key['value'], {
            'maxHitsPerQuery': 42
        }).wait()

        api_key = self.client.get_api_key(response.raw_response['key'])

        self.assertEqual(api_key['maxHitsPerQuery'], 42)

        self.client.delete_api_key(api_key['value']).wait()

        with self.assertRaises(RequestException) as _:
            self.client.get_api_key(api_key['value'])

        self.client.restore_api_key(api_key['value']).wait()

        api_key = self.client.get_api_key(api_key['value'])
        self.assertEqual(api_key['value'],
                         response.raw_response['key'])
        self.client.delete_api_key(api_key['value'])

    def test_get_logs(self):

        self.assertIsInstance(self.client.list_indices(), dict)
        self.assertIsInstance(self.client.list_indices()['items'], list)

        logs = self.client.get_logs({
            'length': 2,
            'offset': 0,
            'type': 'all'
        })['logs']

        self.assertEqual(len(logs), 2)

    def test_multiple_operations(self):
        index_name1 = self.index.name

        index_2 = F.index(self._testMethodName)
        index_name2 = index_2.name

        raw_response = self.client.multiple_batch([
            {"indexName": index_name1, "action": "addObject",
             "body": {"firstname": "Jimmie"}},
            {"indexName": index_name1, "action": "addObject",
             "body": {"firstname": "Jimmie"}},
            {"indexName": index_name2, "action": "addObject",
             "body": {"firstname": "Jimmie"}},
            {"indexName": index_name2, "action": "addObject",
             "body": {"firstname": "Jimmie"}}
        ]).wait().raw_response

        object_ids = list(
            map(lambda object_id: object_id, raw_response['objectIDs']))

        objects = self.client.multiple_get_objects([
            {"indexName": index_name1, "objectID": object_ids[0]},
            {"indexName": index_name1, "objectID": object_ids[1]},
            {"indexName": index_name2, "objectID": object_ids[2]},
            {"indexName": index_name2, "objectID": object_ids[3]}
        ])['results']

        self.assertEqual(objects[0]['objectID'], object_ids[0])
        self.assertEqual(objects[1]['objectID'], object_ids[1])
        self.assertEqual(objects[2]['objectID'], object_ids[2])
        self.assertEqual(objects[3]['objectID'], object_ids[3])

        results = self.client.multiple_queries([
            {"indexName": index_name1,
             "params": QueryParametersSerializer.serialize(
                 {"query": "", "hitsPerPage": 2})},
            {"indexName": index_name2,
             "params": QueryParametersSerializer.serialize(
                 {"query": "", "hitsPerPage": 2})},
        ], {'strategy': 'none'})['results']

        self.assertEqual(len(results), 2)
        self.assertEqual(len(results[0]['hits']), 2)
        self.assertEqual(results[0]['nbHits'], 4)
        self.assertEqual(len(results[1]['hits']), 2)
        self.assertEqual(results[1]['nbHits'], 4)

        results = self.client.multiple_queries([
            {"indexName": index_name1,
             "params": QueryParametersSerializer.serialize(
                 {"query": "", "hitsPerPage": 2})},
            {"indexName": index_name2,
             "params": QueryParametersSerializer.serialize(
                 {"query": "", "hitsPerPage": 2})}

        ], {'strategy': 'stopIfEnoughMatches'})['results']

        self.assertEqual(len(results), 2)
        self.assertEqual(len(results[0]['hits']), 2)
        self.assertEqual(results[0]['nbHits'], 4)
        self.assertEqual(len(results[1]['hits']), 0)
        self.assertEqual(results[1]['nbHits'], 0)

        index_2.delete()

    def test_dns_timeout(self):

        config = SearchConfig(F.get_app_id(), F.get_api_key())

        config.hosts = HostsCollection([
            Host('algolia.biz', 10),
            Host('{}-1.algolianet.com'.format(F.get_app_id())),
            Host('{}-2.algolianet.com'.format(F.get_app_id())),
            Host('{}-3.algolianet.com'.format(F.get_app_id()))
        ])

        client = SearchClient.create_with_config(config)

        client.list_indices()
        # We test that the first Host `algolia.biz` is down.
        self.assertFalse(config.hosts.read()[0].up)
        self.assertTrue(config.hosts.read()[1].up)
        self.assertTrue(config.hosts.read()[2].up)
        self.assertTrue(config.hosts.read()[3].up)

    def test_secured_api_keys(self):
        self.index2 = F.index('{}_dev'.format(self._testMethodName))

        self.index.save_object({'objectID': 'one'}).wait()
        self.index2.save_object({'objectID': 'one'}).wait()

        api_key = self.client.generate_secured_api_key(
            os.environ['ALGOLIA_SEARCH_KEY_1'],
            {
                "validUntil": int(round(time.time())) + (60 * 10),  # + 10 min
                "restrictIndices": self.index.name
            }
        )

        F.search_client(api_key=api_key).init_index(self.index.name).search('')

        with self.assertRaises(RequestException) as _:
            F.search_client(api_key=api_key).init_index(
                self.index2.name).search('')

    @unittest.skipIf(Env.is_community(),
                     "Community can not test personalization operations")
    def test_personalization_strategy(self):
        response = self.client.get_personalization_strategy()
        self.assertIn('taskID', response)

    @unittest.skipIf(os.environ.get('TEST_TYPE', False) != 'async',
                     'Specific asnyc tests')
    def test_async_session(self):
        app_id = Factory.get_app_id()
        api_key = Factory.get_api_key()

        client = SearchClient.create(app_id, api_key)

        import asyncio

        result = asyncio.get_event_loop().run_until_complete(
            asyncio.gather(client.list_api_keys_async())
        )
        self.assertIsInstance(result, list)

        asyncio.get_event_loop().run_until_complete(
            asyncio.gather(client.close())
        )

        self.assertTrue(
            client._transporter_async._requester._session.closed
        )
