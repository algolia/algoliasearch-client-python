import time

import unittest

from tests.features.helpers.factory import Factory


class TestSearchIndex(unittest.TestCase):
    def setUp(self):
        self.index = Factory.index(self._testMethodName)
        self.obj = Factory.obj()

    def test_tasks(self):
        task_id = self.index.save_object(self.obj)['taskID']
        task = self.index.get_task(task_id + 1000000)
        self.assertEqual(task['status'], 'notPublished')

    def test_indexing(self):
        obj_id = self.obj['objectID']
        self.index.save_object(self.obj).wait()

        self.assertEqual(self.obj['name'],
                         self.index.get_object(obj_id)['name'])

    def tearDown(self):
        # self.index.delete()
        pass
