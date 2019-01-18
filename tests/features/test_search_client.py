import unittest

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
