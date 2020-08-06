import json
import calendar
import datetime
import decimal
import sys

from typing import Union, Any, Dict

from algoliasearch.helpers import get_items

# Python 3
if sys.version_info >= (3, 0):
    from urllib.parse import urlencode
else:
    from urllib import urlencode  # pragma: no cover


class QueryParametersSerializer(object):
    @staticmethod
    def serialize(query_parameters):
        # type: (Dict[str, Any]) -> str

        for key, value in get_items(query_parameters):
            if isinstance(value, (list, dict)):
                value = json.dumps(value)
            elif isinstance(value, bool):
                value = "true" if value else "false"

            query_parameters[key] = value

        return urlencode(sorted(get_items(query_parameters), key=lambda val: val[0]))


class SettingsDeserializer(object):
    @staticmethod
    def deserialize(data):
        # type: (Dict[str, Any]) -> dict

        keys = {
            "attributesToIndex": "searchableAttributes",
            "numericAttributesToIndex": "numericAttributesForFiltering",
            "slaves": "replicas",
        }

        for deprecated_key, current_key in get_items(keys):
            if deprecated_key in data:
                data[current_key] = data.pop(deprecated_key)

        return data


class DataSerializer(object):
    @staticmethod
    def serialize(data):
        # type: (Union[Dict[str, Any], list]) -> str

        return json.dumps(data, cls=JSONEncoder)


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        # type: (object) -> object

        if isinstance(obj, decimal.Decimal):
            return float(obj)
        elif isinstance(obj, datetime.datetime):
            return int(calendar.timegm(obj.utctimetuple()))
        elif type(obj).__str__ is not object.__str__:
            return str(obj)

        return json.JSONEncoder.default(self, obj)
