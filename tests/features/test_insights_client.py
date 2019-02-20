import unittest

from tests.helpers.env import Env
from tests.helpers.factory import Factory as F


class TestInsightsClient(unittest.TestCase):
    def setUp(self):
        self.client = F.insights_client()
        self.index = F.index(self._testMethodName)

    def tearDown(self):
        self.index.delete()

    @unittest.skipIf(Env.is_community(),
                     "Community can not test insights operations")
    def test_clicked_object_ids(self):
        user_insights_client = self.client.user('userToken')
        response = user_insights_client.clicked_object_ids('eventName',
                                                           self.index.name,
                                                           ['obj1', 'obj2'])
        self.assertTrue(response['status'] == 200)
        self.assertTrue(response['message'] == 'OK')

    @unittest.skipIf(Env.is_community(),
                     "Community can not test insights operations")
    def test_clicked_object_ids_after_search(self):
        self.index.save_object({'objectID': 'obj1'}).wait()

        query_id = self.index.search('query', {
            'clickAnalytics': True
        })['queryID']

        user_insights_client = self.client.user('userToken')
        response = user_insights_client.clicked_object_ids_after_search(
            'eventName', self.index.name, ['obj1', 'obj2'],
            [1, 2], query_id)
        self.assertTrue(response['status'] == 200)
        self.assertTrue(response['message'] == 'OK')

    @unittest.skipIf(Env.is_community(),
                     "Community can not test insights operations")
    def test_clicked_filters(self):
        user_insights_client = self.client.user('userToken')
        response = user_insights_client.clicked_filters('eventName',
                                                        self.index.name,
                                                        ['filter:foo',
                                                         'filter:bar'])
        self.assertTrue(response['status'] == 200)
        self.assertTrue(response['message'] == 'OK')

    @unittest.skipIf(Env.is_community(),
                     "Community can not test insights operations")
    def test_converted_object_ids(self):
        user_insights_client = self.client.user('userToken')
        response = user_insights_client.converted_object_ids('eventName',
                                                             self.index.name,
                                                             ['obj1', 'obj2'])
        self.assertTrue(response['status'] == 200)
        self.assertTrue(response['message'] == 'OK')

    @unittest.skipIf(Env.is_community(),
                     "Community can not test insights operations")
    def test_converted_object_ids_after_search(self):
        self.index.save_object({'objectID': 'obj1'}).wait()

        query_id = self.index.search('query', {
            'clickAnalytics': True
        })['queryID']

        user_insights_client = self.client.user('userToken')
        response = user_insights_client.converted_object_ids_after_search(
            'eventName', self.index.name, ['obj1', 'obj2'],
            query_id)
        self.assertTrue(response['status'] == 200)
        self.assertTrue(response['message'] == 'OK')

    @unittest.skipIf(Env.is_community(),
                     "Community can not test insights operations")
    def test_converted_filters(self):
        user_insights_client = self.client.user('userToken')
        response = user_insights_client.converted_filters('eventName',
                                                          self.index.name,
                                                          ['filter:foo',
                                                           'filter:bar'])
        self.assertTrue(response['status'] == 200)
        self.assertTrue(response['message'] == 'OK')

    @unittest.skipIf(Env.is_community(),
                     "Community can not test insights operations")
    def test_viewed_object_ids(self):
        user_insights_client = self.client.user('userToken')
        response = user_insights_client.viewed_object_ids('eventName',
                                                          self.index.name,
                                                          ['obj1', 'obj2'])
        self.assertTrue(response['status'] == 200)
        self.assertTrue(response['message'] == 'OK')

    @unittest.skipIf(Env.is_community(),
                     "Community can not test insights operations")
    def test_viewed_filters(self):
        user_insights_client = self.client.user('userToken')
        response = user_insights_client.viewed_filters('eventName',
                                                       self.index.name,
                                                       ['filter:foo',
                                                        'filter:bar'])
        self.assertTrue(response['status'] == 200)
        self.assertTrue(response['message'] == 'OK')
