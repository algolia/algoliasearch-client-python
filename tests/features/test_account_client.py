import os
import unittest

from algoliasearch.account_client import AccountClient
from algoliasearch.exceptions import AlgoliaException
from algoliasearch.responses import MultipleResponse
from tests.helpers.factory import Factory as F


class TestAccountClient(unittest.TestCase):
    def setUp(self):
        self.client1 = F.search_client()
        self.client2 = F.search_client2()
        self.index = F.index(self.client1, self._testMethodName)
        self.index2 = F.index(self.client2, self._testMethodName)

    def tearDown(self):
        self.client1.close()
        self.client2.close()

    @unittest.skipIf(os.environ.get('TEST_TYPE', False) == 'async',
                     'Cross App Copy Index is not available in async mode.')
    def test_cross_app_copy_index(self):
        rule = F.rule(object_id='one')
        synonym = F.synonym(object_id='one')
        responses = [
            self.index.save_object({'objectID': 'one'}),
            self.index.save_rule(rule),
            self.index.save_synonym(synonym),
            self.index.set_settings({'searchableAttributes': ['objectID']})
        ]

        MultipleResponse(responses).wait()

        AccountClient.copy_index(self.index, self.index2).wait()

        # Assert objects got copied
        res = self.index2.search('')

        self.assertEqual(len(res['hits']), 1)
        self.assertEqual(res['hits'][0], {'objectID': 'one'})

        # Assert settings got copied
        settings = self.index2.get_settings()
        self.assertEqual(settings['searchableAttributes'], ['objectID'])

        # Assert synonyms got copied
        self.assertEqual(self.index2.get_rule('one'), rule)

        # Assert synonyms got copied
        list_synonyms1 = [synonym for synonym in self.index.browse_synonyms()]
        list_synonyms2 = [synonym for synonym in self.index2.browse_synonyms()]

        self.assertEqual(list_synonyms1, list_synonyms2)

        # Assert synomys are the same
        self.assertEqual(self.index2.get_synonym('one'), synonym)

        # Assert that copying again fails because index already exists
        with self.assertRaises(AlgoliaException) as _:
            AccountClient.copy_index(self.index, self.index2)
