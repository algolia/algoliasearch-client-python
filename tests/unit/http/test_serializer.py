import datetime
import decimal
import json
import unittest

from algoliasearch.http.serializer import Serializer


class TestSerializer(unittest.TestCase):
    def setUp(self):
        self.data = {
            'decimal': decimal.Decimal(0.20),
            'datetime': datetime.date.today(),
            'value': 'foo',
            'integer': 1
        }

    def test_result(self):
        expected = {
            "decimal": 0.2,
            "datetime": "2019-01-04",
            "value": "foo",
            "integer": 1
        }

        data = Serializer.serialize(self.data)

        self.assertEqual(data, json.dumps(expected))
