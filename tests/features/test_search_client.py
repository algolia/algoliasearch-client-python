import datetime
import os
import platform
import unittest

import time

from algoliasearch.configs import SearchConfig
from algoliasearch.exceptions import RequestException, \
    ValidUntilNotFoundException
from algoliasearch.http.serializer import QueryParametersSerializer
from algoliasearch.responses import MultipleResponse
from algoliasearch.search_client import SearchClient
from tests.helpers.env import Env
from tests.helpers.factory import Factory as F, Factory


class TestSearchClient(unittest.TestCase):
    def setUp(self):
        self.client = F.search_client()
        self.index = F.index(self.client, self._testMethodName)

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

        index2 = F.index(self.client, '{}_settings'.format(self._testMethodName))  # noqa: E501
        responses.push(self.client.copy_settings(
            self.index.name, index2.name
        ))

        index3 = F.index(self.client, '{}_rules'.format(self._testMethodName))  # noqa: E501
        responses.push(self.client.copy_rules(
            self.index.name, index3.name
        ))

        index4 = F.index(self.client, '{}_synonyms'.format(self._testMethodName))  # noqa: E501
        responses.push(self.client.copy_synonyms(
            self.index.name, index4.name
        ))

        index5 = F.index(self.client, '{}_full_copy'.format(self._testMethodName))  # noqa: E501
        responses.push(self.client.copy_index(
            self.index.name, index5.name
        ))

        responses.wait()

        self.assertEqual(
            index2.get_settings()['attributesForFaceting'], ['company']
        )

        index3.get_rule('company_auto_faceting')
        with self.assertRaises(RequestException) as cm:
            index3.get_synonym('google_placeholder')

        index4.get_synonym('google_placeholder')
        with self.assertRaises(RequestException) as cm:
            index4.get_rule('company_auto_faceting')

        index5.get_synonym('google_placeholder')
        index5.get_rule('company_auto_faceting')
        self.assertEqual(
            index5.get_settings()['attributesForFaceting'], ['company']
        )
        for obj in index5.browse_objects():
            self.assertIn(obj, objects)

        index6 = F.index(self.client, '{}_after_move'.format(self._testMethodName))  # noqa: E501
        self.client.move_index(
            self.index.name,
            index6.name
        ).wait()

        index6.get_synonym('google_placeholder')
        index6.get_rule('company_auto_faceting')
        self.assertEqual(
            index6.get_settings()['attributesForFaceting'], ['company']
        )
        for obj in index6.browse_objects():
            self.assertIn(obj, objects)

        with self.assertRaises(RequestException) as cm:
            self.client.init_index(self.index.name).search('')

        self.assertEqual(cm.exception.status_code, 404)

    @unittest.skipIf(Env.is_community(),
                     "Community can not test mcm operations")
    def test_mcm(self):
        mcm = F.search_client_mcm()

        clusters = mcm.list_clusters()['clusters']
        self.assertEqual(len(clusters), 2)

        cluster_name = clusters[0]['clusterName']

        date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

        if 'TRAVIS' in os.environ:
            instance = os.environ['TRAVIS_JOB_NUMBER']
        else:
            instance = 'unknown'

        python_version = platform.python_version().replace('.', '')[:2]

        python_version += os.environ.get('TEST_TYPE', '')

        def user_id(number):
            return 'python{}-{}-{}-{}'.format(
                python_version,
                date,
                instance,
                number
            )

        mcm.assign_user_id(user_id(0), cluster_name)

        mcm.assign_user_ids([user_id(1), user_id(2)], cluster_name)

        def get_user_id(number):
            while True:
                try:
                    return mcm.get_user_id(user_id(number))
                except RequestException as exception:
                    if exception.status_code != 404:
                        raise exception

        for number in range(3):
            self.assertEqual(get_user_id(number), {
                'userID': user_id(number),
                'clusterName': cluster_name,
                'nbRecords': 0,
                'dataSize': 0,
            })

        for number in range(3):
            users_ids = [user['userID'] for user in mcm.search_user_ids(user_id(number))['hits']]  # noqa: E501

            self.assertIn(
                user_id(number),
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

        def remove_user_id(number):
            while True:
                try:
                    return mcm.remove_user_id(user_id(number))
                except RequestException as exception:
                    if exception.status_code != 400:
                        raise exception

        for number in range(3):
            remove_user_id(number)

        def assert_remove(number):
            while True:
                try:
                    mcm.get_user_id(user_id(number))
                except RequestException as exception:
                    if exception.status_code == 404:
                        return

        for number in range(3):
            assert_remove(number)

        has_pending_mappings = mcm.has_pending_mappings({
            'retrieveMappings': True
        })
        self.assertIsNotNone(has_pending_mappings)
        self.assertIsInstance(has_pending_mappings['pending'], bool)
        self.assertTrue('clusters' in has_pending_mappings)
        self.assertIsInstance(has_pending_mappings['clusters'], dict)

        has_pending_mappings = mcm.has_pending_mappings({
            'retrieveMappings': False
        })
        self.assertIsInstance(has_pending_mappings['pending'], bool)
        self.assertFalse('clusters' in has_pending_mappings)

        has_pending_mappings = mcm.has_pending_mappings()
        self.assertIsInstance(has_pending_mappings['pending'], bool)
        self.assertFalse('clusters' in has_pending_mappings)

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

        result = None
        while result is None:
            try:
                result = self.client.restore_api_key(api_key['value']).wait()
            except RequestException as e:
                if e.message != 'Key already exists':
                    raise e
                pass

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
        index2 = F.index(self.client, "{}2".format(self._testMethodName))
        index_name1 = self.index.name
        index_name2 = index2.name

        raw_response = self.client.multiple_batch([
            {"indexName": index_name1, "action": "addObject", "body": {"firstname": "Jimmie"}},  # noqa: E501
            {"indexName": index_name1, "action": "addObject", "body": {"firstname": "Jimmie"}},  # noqa: E501
            {"indexName": index_name2, "action": "addObject", "body": {"firstname": "Jimmie"}},  # noqa: E501
            {"indexName": index_name2, "action": "addObject", "body": {"firstname": "Jimmie"}}  # noqa: E501
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
            {
                "indexName": index_name1,
                "params": QueryParametersSerializer.serialize({"query": "", "hitsPerPage": 2})  # noqa: E501
            },
            {
                "indexName": index_name2,
                "params": QueryParametersSerializer.serialize({"query": "", "hitsPerPage": 2})  # noqa: E501
            }
        ], {'strategy': 'none'})['results']

        self.assertEqual(len(results), 2)
        self.assertEqual(len(results[0]['hits']), 2)
        self.assertEqual(results[0]['nbHits'], 2)
        self.assertEqual(len(results[1]['hits']), 2)
        self.assertEqual(results[1]['nbHits'], 2)

        results = self.client.multiple_queries([
            {
                "indexName": index_name1,
                "params": QueryParametersSerializer.serialize({"query": "", "hitsPerPage": 2})  # noqa: E501
            },
            {
                "indexName": index_name2,
                "params": QueryParametersSerializer.serialize({"query": "", "hitsPerPage": 2})  # noqa: E501
            }
        ], {'strategy': 'stopIfEnoughMatches'})['results']

        self.assertEqual(len(results), 2)
        self.assertEqual(len(results[0]['hits']), 2)
        self.assertEqual(results[0]['nbHits'], 2)
        self.assertEqual(len(results[1]['hits']), 0)
        self.assertEqual(results[1]['nbHits'], 0)

    def test_secured_api_keys(self):
        hosts = F.hosts(self.client.app_id)

        config1 = SearchConfig(F.get_app_id(), F.get_api_key())
        config1.hosts = hosts
        client1 = F.decide(SearchClient.create_with_config(config1))

        index1 = F.index(client1, self._testMethodName)
        index2 = F.index(client1, '{}_dev'.format(self._testMethodName))

        index1.save_object({'objectID': 'one'}).wait()
        index2.save_object({'objectID': 'one'}).wait()

        api_key = self.client.generate_secured_api_key(
            os.environ['ALGOLIA_SEARCH_KEY_1'],
            {
                "validUntil": int(round(time.time())) + (60 * 10),  # + 10 min
                "restrictIndices": index1.name
            }
        )

        config2 = SearchConfig(F.get_app_id(), api_key)
        config2.hosts = hosts
        client2 = F.decide(SearchClient.create_with_config(config2))

        index1_search = client2.init_index(index1.name)
        index2_search = client2.init_index(index2.name)

        index1_search.search('')
        with self.assertRaises(RequestException) as _:
            index2_search.search('')

    def test_get_secured_api_key_remaining_validity(self):
        import time

        now = int(time.time())
        api_key = SearchClient.generate_secured_api_key('foo', {
            'validUntil': now - (60 * 10)
        })

        remaining = SearchClient.get_secured_api_key_remaining_validity(
            api_key
        )

        self.assertTrue(remaining < 0)

        api_key = SearchClient.generate_secured_api_key('foo', {
            'validUntil': now + (60 * 10),
        })

        remaining = SearchClient.get_secured_api_key_remaining_validity(
            api_key
        )
        self.assertTrue(remaining > 0)

        api_key = SearchClient.generate_secured_api_key('foo', {})

        with self.assertRaises(ValidUntilNotFoundException) as _:
            SearchClient.get_secured_api_key_remaining_validity(api_key)


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
