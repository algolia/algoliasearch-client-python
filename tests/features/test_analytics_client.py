import os
import platform
import unittest
import datetime

from algoliasearch.exceptions import RequestException
from tests.helpers.factory import Factory as F


class TestAnalyticsClient(unittest.TestCase):
    def setUp(self):
        self.client = F.analytics_client()
        self.index = F.index(self._testMethodName)
        self.index2 = F.index(self._testMethodName + '2')

    def tearDown(self):
        self.index.delete()
        self.index2.delete()

    def test_ab_testing(self):
        python_version = platform.python_version().replace('.', '')[:2]
        python_version += os.environ.get('TEST_TYPE', '')
        print(python_version)
        ab_tests = self.client.get_ab_tests()
        if ab_tests['total'] > 0:
            for ab_test in self.client.get_ab_tests()['abtests']:
                if ab_test['name'].startswith('python' + python_version):
                    self.client.delete_ab_test(ab_test['abTestID'])

        self.index.save_object({'objectID': 'one'}).wait()
        self.index2.save_object({'objectID': 'one'}).wait()

        tomorrow = (datetime.datetime.now() + datetime.timedelta(
            days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")

        ab_test_name = str(self.index.name)

        response = self.client.add_ab_test({
            "name": ab_test_name,
            "variants": [
                {"index": self.index.name, "trafficPercentage": 60,
                 "description": "a description"},
                {"index": self.index2.name, "trafficPercentage": 40}
            ],
            "endAt": tomorrow
        })

        self.index.wait_task(response['taskID'])
        ab_test_id = response['abTestID']
        ab_test = self.client.get_ab_test(ab_test_id)
        self.assertEqual(ab_test['name'], ab_test_name)
        self.assertEqual(ab_test['endAt'], tomorrow)
        self.assertEqual(ab_test['status'], 'active')

        found = False
        for ab_test in self.client.get_ab_tests()['abtests']:
            if ab_test['name'] == ab_test_name:
                self.assertEqual(ab_test['endAt'], tomorrow)
                self.assertEqual(ab_test['status'], 'active')
                found = True
        self.assertTrue(found)

        self.client.stop_ab_test(ab_test_id)
        self.index.wait_task(response['taskID'])
        ab_test = self.client.get_ab_test(ab_test_id)
        self.assertEqual(ab_test['status'], 'stopped')

        response = self.client.delete_ab_test(ab_test_id)
        self.index.wait_task(response['taskID'])

        with self.assertRaises(RequestException) as _:
            self.client.get_ab_test(ab_test_id)
