import datetime
import decimal
import json
import unittest

from algoliasearch.http.serializer import DataSerializer, \
    QueryParametersSerializer, SettingsDeserializer


class TestDataSerializer(unittest.TestCase):
    def setUp(self):
        self.data = {
            'decimal': decimal.Decimal(0.20),
            'datetime': datetime.datetime(2012, 9, 6),
            'value': 'foo',
            'integer': 1,
            'json': {
                'foo': 'bar'
            },
            'objToString': FakeObjectSerializable()
        }

    def test_result(self):
        expected = {
            'decimal': 0.2,
            'datetime': 1346889600,
            'value': 'foo',
            'integer': 1,
            'json': {
                'foo': 'bar'
            },
            'objToString': 'foo',
        }

        data = DataSerializer.serialize(self.data)

        self.assertEqual(data, json.dumps(expected))

        with self.assertRaises(TypeError) as _:
            DataSerializer.serialize({
                'obj': FakeObject()
            })


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


class TestSettingsDeserializer(unittest.TestCase):
    def setUp(self):
        self.data = {
            'attributesToIndex': 'bar 1',
            'numericAttributesToIndex': 'bar 2',
            'slaves': 'bar 3',
            'foo': 'bar 4',
        }

    def test_result(self):
        expected = {
            'searchableAttributes': 'bar 1',
            'numericAttributesForFiltering': 'bar 2',
            'replicas': 'bar 3',
            'foo': 'bar 4',  # Should keep this one
        }

        data = SettingsDeserializer.deserialize(self.data)
        self.assertEqual(data, expected)


class FakeObject(object):
    pass


class FakeObjectSerializable(object):
    def __str__(self):
        return 'foo'
