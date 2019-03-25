import json
import unittest

from algoliasearch.exceptions import MissingObjectIdException
from algoliasearch.helpers import assert_object_id


class TestHelpers(unittest.TestCase):

    def test_assert_object_id(self):
        obj = {'foo': 'bar'}
        with self.assertRaises(MissingObjectIdException) as cm:
            assert_object_id([obj])

        exception = cm.exception
        self.assertEqual(
            str(exception),
            'Missing `objectID` in: {"foo": "bar"}'
        )

        self.assertEqual(exception.obj, obj)

        obj['objectID'] = 1

        assert_object_id([obj])
