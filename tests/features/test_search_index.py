# -*- coding: utf-8 -*-
import sys
import unittest

from algoliasearch.exceptions import RequestException, ObjectNotFoundException
from algoliasearch.responses import MultipleResponse
from algoliasearch.search_index import SearchIndex
from tests.helpers.factory import Factory as F
from tests.helpers.misc import Unicode


class TestSearchIndex(unittest.TestCase):
    def setUp(self):
        client = F.search_client()
        self.index = F.index(client, self._testMethodName)

    def test_tasks(self):
        task_id = self.index.save_object(F.obj()).raw_responses[0]['taskID']

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
        obj3 = F.obj({'_tags': ['algolia']})
        obj4 = F.obj({'_tags': ['algolia']})
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

        self.index._config.batch_size = 100
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

        responses.append(self.index.delete_by({'tagFilters': ['algolia']}))
        responses.append(self.index.delete_objects([
            object5_id, object6_id
        ]))

        # Delete the 1000 remaining records with delete_objects
        responses.append(self.index.clear_objects())

        MultipleResponse(responses).wait()

        objects = [obj for obj in self.index.browse_objects()]

        self.assertEqual(len(objects), 0)

    def test_settings(self):
        self.index.save_object(F.obj()).wait()

        settings = {
            'searchableAttributes': [
                'attribute1',
                'attribute2',
                'attribute3',
                'ordered(attribute4)',
                'unordered(attribute5)',
            ],
            'attributesForFaceting': [
                'attribute1',
                'filterOnly(attribute2)',
                'searchable(attribute3)',
            ],
            'unretrievableAttributes': [
                'attribute1',
                'attribute2',
            ],
            'attributesToRetrieve': [
                'attribute3',
                'attribute4',
            ],
            'ranking': [
                'asc(attribute1)',
                'desc(attribute2)',
                'attribute',
                'custom',
                'exact',
                'filters',
                'geo',
                'proximity',
                'typo',
                'words',
            ],
            'customRanking': [
                'asc(attribute1)',
                'desc(attribute1)',
            ],
            'replicas': [
                self.index.name + '_replica1',
                self.index.name + '_replica2',
            ],
            'maxValuesPerFacet': 100,
            'sortFacetValuesBy': 'count',
            'attributesToHighlight': [
                'attribute1',
                'attribute2'
            ],
            'attributesToSnippet': [
                'attribute1:10',
                'attribute2:8',
            ],
            'highlightPreTag': '<strong>',
            'highlightPostTag': '</strong>',
            'snippetEllipsisText': ' and so on.',
            'restrictHighlightAndSnippetArrays': True,
            'hitsPerPage': 42,
            'paginationLimitedTo': 43,
            'minWordSizefor1Typo': 2,
            'minWordSizefor2Typos': 6,
            'typoTolerance': 'false',
            'allowTyposOnNumericTokens': False,
            'ignorePlurals': True,
            'disableTypoToleranceOnAttributes': [
                'attribute1',
                'attribute2',
            ],
            'disableTypoToleranceOnWords': [
                'word1',
                'word2',
            ],
            'separatorsToIndex': '()[]',
            'queryType': 'prefixNone',
            'removeWordsIfNoResults': 'allOptional',
            'advancedSyntax': True,
            'optionalWords': [
                'word1',
                'word2',
            ],
            'removeStopWords': True,
            'disablePrefixOnAttributes': [
                'attribute1',
                'attribute2',
            ],
            'disableExactOnAttributes': [
                'attribute1',
                'attribute2'
            ],
            'exactOnSingleWordQuery': 'word',
            'enableRules': False,
            'numericAttributesForFiltering': [
                'attribute1',
                'attribute2',
            ],
            'allowCompressionOfIntegerArray': True,
            'attributeForDistinct': 'attribute1',
            'distinct': 2,
            'replaceSynonymsInHighlight': False,
            'minProximity': 7,
            'responseFields': [
                'hits',
                'hitsPerPage'
            ],
            'maxFacetHits': 100,
            'camelCaseAttributes': [
                'attribute1',
                'attribute2',
            ],
            'decompoundedAttributes': {
                'de': ['attribute1', 'attribute2'],
                'fi': ['attribute3'],
            },
            'keepDiacriticsOnCharacters': 'øé',
            'queryLanguages': [
                'en',
                'fr',
            ],
            'alternativesAsExact': ['ignorePlurals'],
            'advancedSyntaxFeatures': ['exactPhrase'],
            'userData': {
                'customUserData': 42.0,
            },
            'indexLanguages': ['ja'],
        }

        self.index.set_settings(settings).wait()

        # Because the response settings dict contains the extra version key, we
        # also add it to the expected settings dict to prevent the test to fail
        # for a missing key.
        settings['version'] = 2

        # In case something is wrong, we disable the maximum diff length to be
        # able to see which setting is incorrect.
        self.maxDiff = None

        found = self.index.get_settings()

        self.assertEqual(
            self.index.get_settings(),
            Unicode.convert_dict_to_unicode(settings),
        )

        settings['typoTolerance'] = 'min'
        settings['ignorePlurals'] = ["en", "fr"]
        settings['removeStopWords'] = ["en", "fr"]
        settings['distinct'] = True

        self.index.set_settings(settings).wait()

        self.assertEqual(
            self.index.get_settings(),
            Unicode.convert_dict_to_unicode(settings),
        )

        # To prevent issues in other test, we reset the maximum diff length to
        # its default value
        self.maxDiff = 80 * 8

    def test_search(self):
        responses = MultipleResponse()

        responses.push(self.index.save_objects([
            {"company": "Algolia", "name": "Julien Lemoine",
             "objectID": "julien-lemoine"},  # noqa: E501
            {"company": "Algolia", "name": "Nicolas Dessaigne",
             "objectID": "nicolas-dessaigne"},  # noqa: E501
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
        self.assertEqual(SearchIndex.get_object_position(
            result, 'nicolas-dessaigne'), 0
        )
        self.assertEqual(SearchIndex.get_object_position(
            result, 'julien-lemoine'), 1
        )

        self.assertEqual(SearchIndex.get_object_position(result, ''), -1)

        # Call find_object with the following parameters and check that
        # no object is found
        with self.assertRaises(ObjectNotFoundException):
            self.index.find_object(lambda _: False)

        # Call find_object with the following parameters and check that
        # the first object is returned with a `position=0` and `page=0`
        found = self.index.find_object(lambda _: True)
        self.assertEqual(found['position'], 0)
        self.assertEqual(found['page'], 0)

        def callback(obj):
            # type: (dict) -> bool
            return obj.get('company') == 'Apple'

        # Call find_object with the following parameters and check that
        # no object is found
        with self.assertRaises(ObjectNotFoundException):
            self.index.find_object(callback, {
                'query': 'algolia'
            })

        # Call find_object with the following parameters and check that
        # no object is found
        with self.assertRaises(ObjectNotFoundException):
            self.index.find_object(callback, {
                'query': '',
                'paginate': False,
                'hitsPerPage': 5
            })

        # Call find_object with the following parameters and check that
        # the first object is returned with a `position=0` and `page=2`
        found = self.index.find_object(callback, {
            'query': '',
            'paginate': True,
            'hitsPerPage': 5
        })

        self.assertEqual(found['position'], 0)
        self.assertEqual(found['page'], 2)

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

        result = self.index.search_for_facet_values('company', 'a')[
            'facetHits']

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
            'attributesForFaceting': ['brand', 'model']
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
            "description": "Automatic apply the faceting on `brand` if a"
        }

        responses.push(self.index.save_rule(rule1))

        rule2 = {
            "objectID": "query_edits",
            "condition": {
                "anchoring": "is",
                "pattern": "mobile phone",
                "alternatives": True
            },
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

        rule3 = {
            "objectID": "query_promo",
            "consequence": {
                "params": {
                    "filters": "brand:OnePlus"
                }
            }
        }

        rule4 = {
            "objectID": "query_promo_only_summer",
            "condition": {
                "context": "summer"
            },
            "consequence": {
                "params": {
                    "filters": "model:One"
                }
            }
        }

        responses.push(self.index.save_rules([rule2, rule3, rule4]))

        responses.wait()

        # Should be only the One Plus model One
        self.assertEqual(self.index.search('', {
            'ruleContexts': ['summer']
        })['nbHits'], 1)

        self.assertEqual(self.index.get_rule(rule1['objectID']),
                         rule1)
        self.assertEqual(self.index.get_rule(rule2['objectID']),
                         rule2)

        self.assertEqual(self.index.get_rule(rule3['objectID']),
                         rule3)

        self.assertEqual(self.index.get_rule(rule4['objectID']),
                         rule4)

        self.assertEqual(self.index.search_rules('')['nbHits'], 4)

        # Browse all records with browse_rules
        results = []
        for obj in self.index.browse_rules():
            results.append(obj)

        rules = [
            rule1,
            rule2,
            rule3,
            rule4
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

    def test_batching(self):
        responses = MultipleResponse()

        responses.push(self.index.save_objects([
            {"objectID": "one", "key": "value"},
            {"objectID": "two", "key": "value"},
            {"objectID": "three", "key": "value"},
            {"objectID": "four", "key": "value"},
            {"objectID": "five", "key": "value"},
        ]))

        responses.push(self.index.batch([
            {
                "action": "addObject",
                "body": {"objectID": "zero", "key": "value"}
            },
            {
                "action": "updateObject",
                "body": {"objectID": "one", "k": "v"}
            },
            {
                "action": "partialUpdateObject",
                "body": {"objectID": "two", "k": "v"}
            },
            {
                "action": "partialUpdateObject",
                "body": {"objectID": "two_bis", "key": "value"}
            },
            {
                "action": "partialUpdateObjectNoCreate",
                "body": {"objectID": "three", "k": "v"}
            },
            {
                "action": "deleteObject",
                "body": {"objectID": "four"}
            }
        ]))

        responses.wait()

        objects = [
            {"objectID": "zero", "key": "value"},
            {"objectID": "one", "k": "v"},
            {"objectID": "two", "key": "value", "k": "v"},
            {"objectID": "two_bis", "key": "value"},
            {"objectID": "three", "key": "value", "k": "v"},
            {"objectID": "five", "key": "value"},
        ]

        results = [obj for obj in self.index.browse_objects()]

        for obj in objects:
            self.assertIn(obj, results)

    def test_replacing(self):
        responses = MultipleResponse()
        responses.push(self.index.save_object({"objectID": "one"}))
        responses.push(self.index.save_rule(F.rule(object_id="one")))

        responses.push(self.index.save_synonym(
            {"objectID": "one", "type": "synonym", "synonyms": ["one", "two"]}
        ))

        responses.wait()

        responses.push(self.index.replace_all_objects([{"objectID": "two"}]))
        responses.push(self.index.replace_all_rules([{
            "objectID": "two",
            "condition": {"anchoring": "is", "pattern": "pattern"},
            "consequence": {
                "params": {
                    "query": {
                        "edits": [
                            {"type": "remove", "delete": "pattern"}
                        ]
                    }
                }
            }
        }
        ]))

        responses.push(self.index.replace_all_synonyms([
            {"objectID": "two", "type": "synonym", "synonyms": ["one", "two"]}
        ]))

        responses.wait()

        # Check that record with objectID=`one` does not exist
        with self.assertRaises(RequestException) as _:
            self.index.get_object('one')

        # Check that record with objectID=`two` does exist
        self.assertEqual(self.index.get_object('two')['objectID'], 'two')

        # Check that rule with objectID=`one` does not exist
        with self.assertRaises(RequestException) as _:
            self.index.get_rule('one')

        # Check that rule with objectID=`two` does exist
        self.assertEqual(self.index.get_rule('two')['objectID'], 'two')

        # Check that synonym with objectID=`one` does not exist
        with self.assertRaises(RequestException) as _:
            self.index.get_synonym('one')

        # Check that synonym with objectID="two" does exist using getSynonym
        self.assertEqual(self.index.get_synonym('two')['objectID'], 'two')

    def test_safe_replacing(self):

        # Adds dummy object
        self.index.save_object(F.obj()).wait()

        # Calls replace all objects with an object without
        # object id, and with the safe parameter
        self.index.replace_all_objects([{'name': 'two'}], {
            'autoGenerateObjectIDIfNotExist': True,
            'safe': True
        })

        response = self.index.search('')
        self.assertEqual(response['nbHits'], 1)
        hit = response['hits'][0]
        self.assertEqual(hit['name'], 'two')
        self.assertIn('objectID', hit)
        self.assertIn('_highlightResult', hit)

    def test_exists(self):
        self.assertFalse(self.index.exists())
        self.index.save_object(F.obj()).wait()
        self.assertTrue(self.index.exists())
        self.index.delete().wait()
        self.assertFalse(self.index.exists())

    def test_url_encoding(self):
        objects = [
            # unicode
            '中文',

            # bytestring
            'celery-task-meta-c4f1201f-eb7b-41d5-9318-a75a8cfbdaa0',
            b'celery-task-meta-c4f1201f-eb7b-41d5-9318-a75a8cfbdaa0',

            # misc
            'àlgol?a',
            b'\xe4\xb8\xad\xe6\x96\x87',
            '$^^`',
        ]

        if sys.version_info >= (3, 0):
            objects.append("中文".encode('utf-8'))

        self.index.save_objects(
            [{'objectID': object_id} for object_id in objects]).wait()

        for obj in objects:
            self.index.get_object(obj)

    def get_object_id(self, indexing_response, index=0):
        return indexing_response.raw_responses[0]['objectIDs'][index]
