import os
import platform
import unittest
import datetime

from algoliasearch.exceptions import RequestException
from tests.helpers.factory import Factory as F
from tests.helpers.misc import RetryableClient


class TestAnalyticsClient(unittest.TestCase):
    def setUp(self):
        self.client = RetryableClient(F.analytics_client())
        self.index = F.index(self._testMethodName)
        self.index2 = F.index('{}2'.format(self._testMethodName))

    def tearDown(self):
        self.index.delete()
        self.index2.delete()

    def test_ab_testing(self):
        self.clean_ab_tests()

        self.index.save_object({'objectID': 'one'}).wait()
        self.index2.save_object({'objectID': 'one'}).wait()

        tomorrow = (datetime.datetime.now() + datetime.timedelta(
            days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")

        ab_test_name = str(self.index.name)
        with self.assertRaises(RequestException) as _:
            self.client.get_ab_test('foo')

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

        for ab_test in self.client.get_ab_tests({'limit': 999999})['abtests']:
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

    def test_aa_testing(self):
        self.clean_ab_tests()

        self.index.save_object({'objectID': 'one'}).wait()

        ab_test_name = str(self.index.name)

        tomorrow = (datetime.datetime.now() + datetime.timedelta(
            days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")

        response = self.client.add_ab_test({
            "name": ab_test_name,
            "variants": [
                {"index": self.index.name, "trafficPercentage": 90},
                {
                    "index": self.index.name, "trafficPercentage": 10,
                    "customSearchParameters": {
                        "ignorePlurals": True
                    }
                }
            ],
            "endAt": tomorrow
        })

        self.index.wait_task(response['taskID'])

        ab_test = self.client.get_ab_test(response['abTestID'])
        self.assertEqual(ab_test['name'], ab_test_name)
        self.assertEqual(ab_test['endAt'], tomorrow)

        self.assertEqual(ab_test['variants'][0]['trafficPercentage'], 90)
        self.assertEqual(ab_test['variants'][1]['trafficPercentage'], 10)
        self.assertEqual(ab_test['variants'][1]['customSearchParameters'], {
            "ignorePlurals": True
        })

        self.assertEqual(ab_test['status'], 'active')

        response = self.client.delete_ab_test(response['abTestID'])
        self.index.wait_task(response['taskID'])

    def clean_ab_tests(self):
        python_version = 'python{}{}'.format(
            platform.python_version().replace('.', '')[:2],
            os.environ.get('TEST_TYPE', '')
        )

        ab_tests = self.client.get_ab_tests()

        prefix_of_today_tests = '{}_{}'.format(
            python_version,
            datetime.datetime.now().strftime("%Y-%m-%d")
        )

        if ab_tests['total'] > 0:
            for ab_test in self.client.get_ab_tests()['abtests']:
                if ab_test['name'].startswith(python_version):
                    if not ab_test['name'].startswith(prefix_of_today_tests):
                        self.client.delete_ab_test(ab_test['abTestID'])
