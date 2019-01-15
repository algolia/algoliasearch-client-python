import unittest

from algoliasearch.responses import MultipleResponse
from tests.features.helpers.factory import Factory as F


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

        # Browse all records with browse_all
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

    def get_object_id(self, indexing_response, index=0):
        return indexing_response[0]['objectIDs'][index]

    def tearDown(self):
        self.index.delete()
