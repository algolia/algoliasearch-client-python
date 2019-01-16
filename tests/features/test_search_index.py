import unittest

from algoliasearch.exceptions import RequestException
from algoliasearch.responses import MultipleResponse
from tests.helpers.factory import Factory as F


class TestSearchIndex(unittest.TestCase):
    def setUp(self):
        self.index = F.index(self._testMethodName)

    def test_tasks(self):
        task_id = self.index.save_object(F.obj())[0]['taskID']

        task = self.index.get_task(task_id + 1000000)
        self.assertEqual(task['status'], 'notPublished')

    def test_indexing(self):
        responses = []

        # adding a object with object id
        obj1 = F.obj()
        responses.append(self.index.save_object(obj1))

        # adding a object w/o object id
        obj2 = F.obj(object_id=False)
        opts = {'autoGenerateObjectIDIfNotExist': True}
        responses.append(self.index.save_object(obj2, opts))

        # adding two objects with object id
        obj3 = F.obj()
        obj4 = F.obj()
        responses.append(self.index.save_objects([obj3, obj4]))

        # adding two objects w/o object id
        obj5 = F.obj(object_id=False)
        obj6 = F.obj(object_id=False)
        opts = {'autoGenerateObjectIDIfNotExist': True}
        responses.append(self.index.save_objects([obj5, obj6], opts))

        object1_id = self.get_object_id(responses[0])
        object2_id = self.get_object_id(responses[1])
        object3_id = self.get_object_id(responses[2])
        object4_id = self.get_object_id(responses[2], 1)
        object5_id = self.get_object_id(responses[3])
        object6_id = self.get_object_id(responses[3], 1)

        # adding 1000 objects with object id
        objects = []
        for i in range(1000):
            object_id = i
            objects.append({
                'objectID': str(object_id),
                'name': object_id,
            })

        self.index._SearchIndex__config.batch_size = 100
        responses.append(self.index.save_objects(objects))

        # waiting for all responses
        MultipleResponse(responses).wait()

        # Check 6 first records with get_object
        self.assertEqual(obj1['name'],
                         self.index.get_object(object1_id)['name'])
        self.assertEqual(obj2['name'],
                         self.index.get_object(object2_id)['name'])
        self.assertEqual(obj3['name'],
                         self.index.get_object(object3_id)['name'])
        self.assertEqual(obj4['name'],
                         self.index.get_object(object4_id)['name'])
        self.assertEqual(obj5['name'],
                         self.index.get_object(object5_id)['name'])
        self.assertEqual(obj6['name'],
                         self.index.get_object(object6_id)['name'])

        # Check 1000 remaining records with get_objects
        results = self.index.get_objects(range(1000))['results']
        for obj in results:
            self.assertIn(obj, objects)

        self.assertEqual(len(results), len(objects))

        # Browse all records with browse_objects
        results = []
        for obj in self.index.browse_objects():
            results.append(obj)

        for obj in objects:
            self.assertIn(obj, results)

        for obj in [obj1, obj3, obj4]:
            self.assertIn(obj, results)

        self.assertEqual(len(results), 1006)

        responses = []

        # Alter 1 record with partial_update_object
        obj1['name'] = 'This is an altered name'
        responses.append(self.index.partial_update_object(obj1))

        # Alter 2 records with partial_update_objects
        obj3['bar'] = 40
        obj4['foo'] = 30
        responses.append(self.index.partial_update_objects([obj3, obj4]))

        MultipleResponse(responses).wait()

        self.assertEqual(self.index.get_object(object1_id), obj1)
        self.assertEqual(self.index.get_object(object3_id), obj3)
        self.assertEqual(self.index.get_object(object4_id), obj4)

        responses = []

        # Delete the 6 first records with delete_object
        responses.append(self.index.delete_object(object1_id))
        responses.append(self.index.delete_object(object2_id))
        responses.append(self.index.delete_object(object3_id))
        responses.append(self.index.delete_object(object4_id))
        responses.append(self.index.delete_object(object5_id))
        responses.append(self.index.delete_object(object6_id))

        # Delete the 1000 remaining records with delete_objects
        responses.append(self.index.delete_objects(range(1000)))

        MultipleResponse(responses).wait()

        objects = []
        for obj in self.index.browse_objects():
            objects.append(obj)

        self.assertEqual(len(objects), 0)

    def test_settings(self):
        self.index.save_object(F.obj()).wait()

        self.index.set_settings({'searchableAttributes': ['name']}).wait()

        self.assertEqual(
            self.index.get_settings()['searchableAttributes'],
            ['name']
        )

        self.index.set_settings({'typoTolerance': 'min'}).wait()

        self.assertEqual(
            self.index.get_settings()['typoTolerance'],
            'min'
        )

        self.index.set_settings(self.index.get_settings()).wait()

        self.assertEqual(
            self.index.get_settings()['typoTolerance'],
            'min'
        )

        self.assertEqual(
            self.index.get_settings()['searchableAttributes'],
            ['name']
        )

    def test_search(self):
        responses = MultipleResponse()

        responses.push(self.index.save_objects([
            {"company": "Algolia", "name": "Julien Lemoine"},
            {"company": "Algolia", "name": "Nicolas Dessaigne"},
            {"company": "Amazon", "name": "Jeff Bezos"},
            {"company": "Apple", "name": "Steve Jobs"},
            {"company": "Apple", "name": "Steve Wozniak"},
            {"company": "Arista Networks", "name": "Jayshree Ullal"},
            {"company": "Google", "name": "Larry Page"},
            {"company": "Google", "name": "Rob Pike"},
            {"company": "Google", "name": "Serguey Brin"},
            {"company": "Microsoft", "name": "Bill Gates"},
            {"company": "SpaceX", "name": "Elon Musk"},
            {"company": "Tesla", "name": "Elon Musk"},
            {"company": "Yahoo", "name": "Marissa Mayer"}
        ], {'autoGenerateObjectIDIfNotExist': True}))

        responses.push(self.index.set_settings({
            'attributesForFaceting': ["searchable(company)"]
        }))

        responses.wait()

        # Perform a search query using search with the query `algolia` and no
        # parameter and check that the number of returned hits is equal to 2
        result = self.index.search('algolia')
        self.assertEqual(result['nbHits'], 2)

        # Perform a search using search with the query `elon` and the
        # following parameter and check that the queryID field from
        # the response is not empty
        result = self.index.search('elon', {'clickAnalytics': True})
        self.assertIn('queryID', result)

        # Perform a faceted search using search with the query `elon` and the
        # following parameters and check that the number of returned hits is
        # equal to 1
        result = self.index.search('elon', {
            'facets': '*',
            'facetFilters': 'company:tesla'
        })
        self.assertEqual(result['nbHits'], 1)

        # Perform a filtered search using search with the query `elon` and the
        # following parameters and check that the number of returned hits is
        # equal to 2
        result = self.index.search('elon', {
            'facets': '*',
            'filters': '(company:tesla OR company:spacex)'
        })

        self.assertEqual(result['nbHits'], 2)

        result = self.index.search_for_facet_value('company', 'a')['facetHits']
        values = list(
            map(lambda facet: facet['value'], result))

        self.assertIn('Algolia', values)
        self.assertIn('Amazon', values)
        self.assertIn('Apple', values)
        self.assertIn('Arista Networks', values)

    def test_synonyms(self):
        responses = MultipleResponse()

        responses.push(self.index.save_objects([
            {"console": "Sony PlayStation <PLAYSTATIONVERSION>"},
            {"console": "Nintendo Switch"},
            {"console": "Nintendo Wii U"},
            {"console": "Nintendo Game Boy Advance"},
            {"console": "Microsoft Xbox"},
            {"console": "Microsoft Xbox 360"},
            {"console": "Microsoft Xbox One"}
        ], {'autoGenerateObjectIDIfNotExist': True}))

        responses.push(self.index.save_synonym(F.synonym({
            'synonyms': [
                "gba",
                "gameboy advance",
                "game boy advance"
            ]
        }, 'gba')))

        synonym1 = {
            'objectID': 'wii_to_wii_u',
            'type': 'onewaysynonym',
            'input': 'wii',
            'synonyms': ['wii U']
        }

        synonym2 = {
            'objectID': 'playstation_version_placeholder',
            'type': 'placeholder',
            'placeholder': '<PLAYSTATIONVERSION>',
            'replacements': [
                "1",
                "One",
                "2",
                "3",
                "4",
                "4 Pro",
            ]
        }

        synonym3 = {
            'objectID': 'ps4',
            'type': 'altcorrection1',
            'word': 'ps4',
            'corrections': ['playstation4']
        }

        synonym4 = {
            'objectID': 'psone',
            'type': 'altcorrection2',
            'word': 'psone',
            'corrections': ['playstationone']
        }

        responses.push(self.index.save_synonyms([
            synonym1,
            synonym2,
            synonym3,
            synonym4
        ]))

        responses.wait()

        self.assertEqual(self.index.get_synonym(synonym1['objectID']),
                         synonym1)
        self.assertEqual(self.index.get_synonym(synonym2['objectID']),
                         synonym2)
        self.assertEqual(self.index.get_synonym(synonym3['objectID']),
                         synonym3)
        self.assertEqual(self.index.get_synonym(synonym4['objectID']),
                         synonym4)

        self.assertEqual(self.index.search_synonyms('')['nbHits'], 5)

        # Browse all records with browse_objects
        results = []
        for obj in self.index.browse_synonyms():
            results.append(obj)

        synonyms = [
            synonym1,
            synonym2,
            synonym3,
            synonym4
        ]

        for synonym in synonyms:
            self.assertIn(synonym, results)

        self.index.delete_synonym('gba').wait()

        # Try to get the synonym with getSynonym with objectID `gba and c
        # heck that the synonym does not exist anymore
        with self.assertRaises(RequestException) as _:
            self.index.get_synonym('gba')

        # Clear all the synonyms using clear_synonyms
        self.index.clear_synonyms().wait()

        # Perform a synonym search using searchSynonyms with an empty query
        # and check that the number of returned synonyms is equal to 0
        self.assertEqual(self.index.search_synonyms('')['nbHits'], 0)

    def test_rules(self):
        responses = MultipleResponse()

        responses.push(self.index.save_objects([
            {"objectID": "iphone_7", "brand": "Apple", "model": "7"},
            {"objectID": "iphone_8", "brand": "Apple", "model": "8"},
            {"objectID": "iphone_x", "brand": "Apple", "model": "X"},
            {"objectID": "one_plus_one", "brand": "OnePlus",
             "model": "One"},
            {"objectID": "one_plus_two", "brand": "OnePlus",
             "model": "Two"},
        ]))

        responses.push(self.index.set_settings({
            'attributesForFaceting': ['brand']
        }))

        rule1 = {
            "objectID": "brand_automatic_faceting",
            "enabled": False,
            "condition": {"anchoring": "is", "pattern": "{facet:brand}"},
            "consequence": {
                "params": {
                    "automaticFacetFilters": [
                        {"facet": "brand", "disjunctive": True, "score": 42},
                    ]
                }
            },
            "validity": [
                {
                    "from": 1532439300,
                    "until": 1532525700
                },
                {
                    "from": 1532612100,
                    "until": 1532698500
                }
            ],
            "description": "Automatic apply the faceting on `brand` if a brand value is found in the query"   # noqa: E501

        }

        responses.push(self.index.save_rule(rule1))

        rule2 = {
            "objectID": "query_edits",
            "condition": {"anchoring": "is", "pattern": "mobile phone"},
            "consequence": {
                "params": {
                    "query": {
                        "edits": [
                            {"type": "remove", "delete": "mobile"},
                            {"type": "replace", "delete": "phone",
                             "insert": "iphone"},
                        ]
                    }
                }
            }
        }

        responses.push(self.index.save_rules([rule2]))

        responses.wait()

        self.assertEqual(self.index.get_rule(rule1['objectID']),
                         rule1)
        self.assertEqual(self.index.get_rule(rule2['objectID']),
                         rule2)

        self.assertEqual(self.index.search_rules('')['nbHits'], 2)

        # Browse all records with browse_rules
        results = []
        for obj in self.index.browse_rules():
            results.append(obj)

        rules = [
            rule1,
            rule2,
        ]

        for rule in rules:
            self.assertIn(rule, results)

        self.index.delete_rule(rule1['objectID']).wait()

        # Try to get the first rule with get_rule and check
        # that the rule does not exist anymore
        with self.assertRaises(RequestException) as _:
            self.index.get_rule(rule1['objectID'])

        # Clear all the rules using clear_rules
        self.index.clear_rules().wait()

        # Perform a rule search using search_rule with an empty query
        # and check that the number of returned nbHits is equal to 0
        self.assertEqual(self.index.search_rules('')['nbHits'], 0)

    def get_object_id(self, indexing_response, index=0):
        return indexing_response[0]['objectIDs'][index]

    def tearDown(self):
        self.index.delete()
