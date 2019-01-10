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

        objects = []
        for i in range(1000):
            object_id = i + 1
            objects.append({
                'objectID': object_id,
                'name': object_id
            })

        self.index._SearchIndex__config.batch_size = 100
        responses.append(self.index.save_objects(objects))

        MultipleResponse(responses).wait()

        self.assertDictContainsSubset(obj1, self.index.get_object(
            self.get_object_id(responses[0])))
        self.assertDictContainsSubset(obj2, self.index.get_object(
            self.get_object_id(responses[1])))
        self.assertDictContainsSubset(obj3, self.index.get_object(
            self.get_object_id(responses[2])))

        self.assertDictContainsSubset(obj4, self.index.get_object(
            self.get_object_id(responses[2], 1)))
        self.assertDictContainsSubset(obj5, self.index.get_object(
            self.get_object_id(responses[3])))
        self.assertDictContainsSubset(obj6, self.index.get_object(
            self.get_object_id(responses[3], 1)))

    def get_object_id(self, indexing_response, index=0):
        return indexing_response[0]['objectIDs'][index]

    def tearDown(self):
        self.index.delete()
