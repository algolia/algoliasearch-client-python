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
        try:
            self.client.get_recommendations(
                [
                    {
                        "indexName": "products",
                        "objectID": "B018APC4LE",
                        "model": "bought-together",
                    },
                ]
            )
        except Exception:
            pass

        # Test method with 'related-products' mode
        try:
            self.client.get_recommendations(
                [
                    {
                        "indexName": "products",
                        "objectID": "B018APC4LE",
                        "model": "related-products",
                    },
                ]
            )
        except Exception:
            pass

        # Test method with multiple requests and specified thresholds
        try:
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
        except Exception:
            pass

        # Test overrides undefined threshold with default value
        try:
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
        except Exception:
            pass

        # Test threshold is overriden by specified value
        try:
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
        except Exception:
            pass

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
        try:
            self.client.get_related_products(
                [
                    {
                        "indexName": "products",
                        "objectID": "B018APC4LE",
                    },
                ]
            )
        except Exception:
            pass

        # Test if it overrides wrong given model
        try:
            self.client.get_related_products(
                [
                    {
                        "indexName": "products",
                        "objectID": "B018APC4LE",
                        "model": "bought-together",
                    },
                ]
            )
        except Exception:
            pass

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
        try:
            self.client.get_frequently_bought_together(
                [
                    {
                        "indexName": "products",
                        "objectID": "B018APC4LE",
                    },
                ]
            )
        except Exception:
            pass

        # Test if it overrides wrong given model
        try:
            self.client.get_frequently_bought_together(
                [
                    {
                        "indexName": "products",
                        "objectID": "B018APC4LE",
                    },
                ]
            )
        except Exception:
            pass

        # Test if `fallbackParameters` param is not passed for 'bought-together' method
        try:
            self.client.get_frequently_bought_together(
                [
                    {
                        "indexName": "products",
                        "objectID": "B018APC4LE",
                        "fallbackParameters": {"facetFilters": []},
                    },
                ]
            )
        except Exception:
            pass

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
