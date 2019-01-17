import datetime
import decimal
import json
import unittest

from algoliasearch.http.serializer import DataSerializer, \
    QueryParametersSerializer


class TestDataSerializer(unittest.TestCase):
    def setUp(self):
        self.data = {
            'decimal': decimal.Decimal(0.20),
            'datetime': datetime.date.fromtimestamp(1546300800),
            'value': 'foo',
            'integer': 1
        }

    def test_result(self):
        expected = {
            "decimal": 0.2,
            "datetime": "2019-01-01",
            "value": "foo",
            "integer": 1
        }

        data = DataSerializer.serialize(self.data)

        self.assertEqual(data, json.dumps(expected))


class TestQueryParametersSerializer(unittest.TestCase):
    def setUp(self):
        self.data = {
            'boolean': True,
            'dict': {'foo': 'bar'}
        }

    def test_result(self):
        expected = 'boolean=true&dict=%7B%22foo%22%3A+%22bar%22%7D'

        data = QueryParametersSerializer.serialize(self.data)
        self.assertEqual(data, expected)
