import json
import unittest

from algoliasearch.exceptions import MissingObjectIdException
from algoliasearch.helpers import assert_object_id, endpoint


class TestHelpers(unittest.TestCase):
    def test_assert_object_id(self):
        obj = {"foo": "bar"}
        with self.assertRaises(MissingObjectIdException) as cm:
            assert_object_id([obj])

        exception = cm.exception
        self.assertEqual(str(exception), 'Missing `objectID` in: {"foo": "bar"}')

        self.assertEqual(exception.obj, obj)

        obj["objectID"] = 1

        assert_object_id([obj])

    def test_endpoint(self):

        self.assertEqual("", endpoint(""))

        self.assertEqual(
            "/1/indexes/test/settings", endpoint("/1/indexes/test/settings")
        )

        self.assertEqual(
            "/1/indexes/test/task/123", endpoint("/1/indexes/test/task/{}", 123)
        )

        self.assertEqual(
            "/1/indexes/index%23name/task/1234",
            endpoint("/1/indexes/{}/task/{}", "index#name", 1234),
        )

        self.assertEqual(
            "/1/indexes/%23index%20name_42%23%2523/batch",
            endpoint("/1/indexes/{}/batch", "#index name_42#%23"),
        )

        self.assertEqual(
            "/1/indexes/space%20bar/browse",
            endpoint("/1/indexes/{}/browse", "space bar"),
        )
