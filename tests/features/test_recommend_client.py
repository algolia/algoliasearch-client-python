import json
import requests
from algoliasearch.recommend_client import RecommendClient
import unittest
import mock

# we ignore the `line-too-long` lint errors for the file
# flake8: noqa E501


class TestRecommendClient(unittest.TestCase):
    def setUp(self):
        self.client = RecommendClient.create("foo", "bar")
        # `_session` is initialized with `None` to make it closable, we override it
        # here to mock it.
        self.client._transporter._requester._session = requests.Session()
        self.client._transporter._requester._session.send = mock.Mock(name="send")
        self.client._transporter._requester._session.send.return_value.status_code = 200

    def tearDown(self):
        self.client.close()

    def assert_requests(self, expected):
        for i, raw_req in enumerate(
            self.client._transporter._requester._session.send.call_args_list
        ):
            # req is in `call -> PreparedRequest`
            req = raw_req[0][0]

            self.assertEqual(req.method, expected[i]["method"])
            self.assertEqual(req.path_url, expected[i]["path"])
            self.assertDictEqual(json.loads(req.body), json.loads(expected[i]["body"]))

    def test_get_recommendations(self):
        # Test method with 'bought-together' model
        self.client.get_recommendations(
            [
                {
                    "indexName": "products",
                    "objectID": "B018APC4LE",
                    "model": "bought-together",
                },
            ]
        )

        # Test method with 'related-products' mode
        self.client.get_recommendations(
            [
                {
                    "indexName": "products",
                    "objectID": "B018APC4LE",
                    "model": "related-products",
                },
            ]
        )

        # Test method with multiple requests and specified thresholds
        self.client.get_recommendations(
            [
                {
                    "indexName": "products",
                    "objectID": "B018APC4LE-1",
                    "model": "related-products",
                    "threshold": 0,
                },
                {
                    "indexName": "products",
                    "objectID": "B018APC4LE-2",
                    "model": "related-products",
                    "threshold": 0,
                },
            ]
        )

        # Test overrides undefined threshold with default value
        self.client.get_recommendations(
            [
                {
                    "indexName": "products",
                    "objectID": "B018APC4LE",
                    "model": "related-products",
                    "threshold": None,
                },
            ]
        )

        # Test threshold is overriden by specified value
        self.client.get_recommendations(
            [
                {
                    "indexName": "products",
                    "objectID": "B018APC4LE",
                    "model": "related-products",
                    "threshold": 42,
                },
            ]
        )

        self.assert_requests(
            [
                {
                    "method": "POST",
                    "path": "/1/indexes/*/recommendations",
                    "body": '{"requests":[{"indexName":"products","objectID":"B018APC4LE","model":"bought-together","threshold":0}]}',
                },
                {
                    "method": "POST",
                    "path": "/1/indexes/*/recommendations",
                    "body": '{"requests":[{"indexName":"products","objectID":"B018APC4LE","model":"related-products","threshold":0}]}',
                },
                {
                    "method": "POST",
                    "path": "/1/indexes/*/recommendations",
                    "body": '{"requests":[{"indexName":"products","objectID":"B018APC4LE-1","model":"related-products","threshold":0},{"indexName":"products","objectID":"B018APC4LE-2","model":"related-products","threshold":0}]}',
                },
                {
                    "method": "POST",
                    "path": "/1/indexes/*/recommendations",
                    "body": '{"requests":[{"indexName":"products","objectID":"B018APC4LE","model":"related-products","threshold":0}]}',
                },
                {
                    "method": "POST",
                    "path": "/1/indexes/*/recommendations",
                    "body": '{"requests":[{"indexName":"products","objectID":"B018APC4LE","model":"related-products","threshold":42}]}',
                },
            ]
        )

    def test_get_related_products(self):
        # Test method
        self.client.get_related_products(
            [
                {
                    "indexName": "products",
                    "objectID": "B018APC4LE",
                },
            ]
        )

        # Test if it overrides wrong given model
        self.client.get_related_products(
            [
                {
                    "indexName": "products",
                    "objectID": "B018APC4LE",
                    "model": "bought-together",
                },
            ]
        )

        self.assert_requests(
            [
                {
                    "method": "POST",
                    "path": "/1/indexes/*/recommendations",
                    "body": '{"requests":[{"indexName":"products","objectID":"B018APC4LE","model":"related-products","threshold":0}]}',
                },
                {
                    "method": "POST",
                    "path": "/1/indexes/*/recommendations",
                    "body": '{"requests":[{"indexName":"products","objectID":"B018APC4LE","model":"related-products","threshold":0}]}',
                },
            ]
        )

    def test_get_frequently_bought_together(self):
        # Test method
        self.client.get_frequently_bought_together(
            [
                {
                    "indexName": "products",
                    "objectID": "B018APC4LE",
                },
            ]
        )

        # Test if it overrides wrong given model
        self.client.get_frequently_bought_together(
            [
                {
                    "indexName": "products",
                    "objectID": "B018APC4LE",
                },
            ]
        )

        # Test if `fallbackParameters` param is not passed for 'bought-together' method
        self.client.get_frequently_bought_together(
            [
                {
                    "indexName": "products",
                    "objectID": "B018APC4LE",
                    "fallbackParameters": {"facetFilters": []},
                },
            ]
        )

        self.assert_requests(
            [
                {
                    "method": "POST",
                    "path": "/1/indexes/*/recommendations",
                    "body": '{"requests":[{"indexName":"products","objectID":"B018APC4LE","model":"bought-together","threshold":0}]}',
                },
                {
                    "method": "POST",
                    "path": "/1/indexes/*/recommendations",
                    "body": '{"requests":[{"indexName":"products","objectID":"B018APC4LE","model":"bought-together","threshold":0}]}',
                },
                {
                    "method": "POST",
                    "path": "/1/indexes/*/recommendations",
                    "body": '{"requests":[{"indexName":"products","objectID":"B018APC4LE","model":"bought-together","threshold":0}]}',
                },
            ]
        )
