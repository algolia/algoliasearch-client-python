from algoliasearch.http.transporter import Request
from algoliasearch.recommend_client import RecommendClient
import unittest
import mock


class TestRecommendClient(unittest.TestCase):
    host = "1/indexes/*/recommendations?"

    def setUp(self):
        self.client = RecommendClient.create("foo", "bar")

    def tearDown(self):
        self.client.close()

    def build_request(self, requests):
        req = Request(
            "POST",
            {
                "X-Algolia-Application-Id": "foo",
                "X-Algolia-API-Key": "bar",
                "User-Agent": mock.ANY,
                "Content-Type": "application/json",
            },
            {"requests": requests},
            2,
            5,
            {},
        )

        return req

    def test_get_recommendations(self):
        # Test method with 'bought-together' model
        self.client._transporter.retry = mock.Mock(name="retry")
        self.client.get_recommendations(
            [
                {
                    "indexName": "products",
                    "objectID": "B018APC4LE",
                    "model": "bought-together",
                },
            ]
        )
        self.client._transporter.retry.assert_called_with(
            # we don't check the hosts
            mock.ANY,
            self.build_request(
                [
                    {
                        "indexName": "products",
                        "objectID": "B018APC4LE",
                        "model": "bought-together",
                        "threshold": 0,
                    }
                ]
            ),
            self.host,
        )

        # Test method with 'related-products' mode
        self.client._transporter.retry = mock.Mock(name="retry")
        self.client.get_recommendations(
            [
                {
                    "indexName": "products",
                    "objectID": "B018APC4LE",
                    "model": "related-products",
                },
            ]
        )
        self.client._transporter.retry.assert_called_with(
            # we don't check the hosts
            mock.ANY,
            self.build_request(
                [
                    {
                        "indexName": "products",
                        "objectID": "B018APC4LE",
                        "model": "related-products",
                        "threshold": 0,
                    }
                ]
            ),
            self.host,
        )

        # Test method with multiple requests and specified thresholds
        self.client._transporter.retry = mock.Mock(name="retry")
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
        self.client._transporter.retry.assert_called_with(
            # we don't check the hosts
            mock.ANY,
            self.build_request(
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
            ),
            self.host,
        )

        # Test overrides undefined threshold with default value
        self.client._transporter.retry = mock.Mock(name="retry")
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
        self.client._transporter.retry.assert_called_with(
            # we don't check the hosts
            mock.ANY,
            self.build_request(
                [
                    {
                        "indexName": "products",
                        "objectID": "B018APC4LE",
                        "model": "related-products",
                        "threshold": 0,
                    }
                ]
            ),
            self.host,
        )

        # Test threshold is overriden by specified value
        self.client._transporter.retry = mock.Mock(name="retry")
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
        self.client._transporter.retry.assert_called_with(
            # we don't check the hosts
            mock.ANY,
            self.build_request(
                [
                    {
                        "indexName": "products",
                        "objectID": "B018APC4LE",
                        "model": "related-products",
                        "threshold": 42,
                    }
                ]
            ),
            self.host,
        )

    def test_get_related_products(self):
        self.client._transporter.retry = mock.Mock(name="retry")
        self.client.get_related_products(
            [
                {
                    "indexName": "products",
                    "objectID": "B018APC4LE",
                },
            ]
        )
        self.client._transporter.retry.assert_called_with(
            # we don't check the hosts
            mock.ANY,
            self.build_request(
                [
                    {
                        "indexName": "products",
                        "objectID": "B018APC4LE",
                        "model": "related-products",
                        "threshold": 0,
                    }
                ]
            ),
            self.host,
        )

        # Test if it overrides wrong given model
        self.client._transporter.retry = mock.Mock(name="retry")
        self.client.get_related_products(
            [
                {
                    "indexName": "products",
                    "objectID": "B018APC4LE",
                    "model": "bought-together",
                },
            ]
        )
        self.client._transporter.retry.assert_called_with(
            # we don't check the hosts
            mock.ANY,
            self.build_request(
                [
                    {
                        "indexName": "products",
                        "objectID": "B018APC4LE",
                        "model": "related-products",
                        "threshold": 0,
                    }
                ]
            ),
            self.host,
        )

    def test_get_frequently_bought_together(self):
        self.client._transporter.retry = mock.Mock(name="retry")
        self.client.get_frequently_bought_together(
            [
                {
                    "indexName": "products",
                    "objectID": "B018APC4LE",
                },
            ]
        )
        self.client._transporter.retry.assert_called_with(
            # we don't check the hosts
            mock.ANY,
            self.build_request(
                [
                    {
                        "indexName": "products",
                        "objectID": "B018APC4LE",
                        "model": "bought-together",
                        "threshold": 0,
                    }
                ]
            ),
            self.host,
        )

        # Test if it overrides wrong given model
        self.client._transporter.retry = mock.Mock(name="retry")
        self.client.get_frequently_bought_together(
            [
                {
                    "indexName": "products",
                    "objectID": "B018APC4LE",
                    "model": "related-products",
                },
            ]
        )
        self.client._transporter.retry.assert_called_with(
            # we don't check the hosts
            mock.ANY,
            self.build_request(
                [
                    {
                        "indexName": "products",
                        "objectID": "B018APC4LE",
                        "model": "bought-together",
                        "threshold": 0,
                    }
                ]
            ),
            self.host,
        )

        # Check if `fallbackParameters` param is not passed for 'bought-together' method
        self.client._transporter.retry = mock.Mock(name="retry")
        self.client.get_frequently_bought_together(
            [
                {
                    "indexName": "products",
                    "objectID": "B018APC4LE",
                    "fallbackParameters": {"facetFilters": []},
                },
            ]
        )
        self.client._transporter.retry.assert_called_with(
            # we don't check the hosts
            mock.ANY,
            self.build_request(
                [
                    {
                        "indexName": "products",
                        "objectID": "B018APC4LE",
                        "model": "bought-together",
                        "threshold": 0,
                    }
                ]
            ),
            self.host,
        )
