import json
import calendar
import datetime
import decimal
import sys

from typing import Union

from algoliasearch.helpers import get_items

# Python 3
if sys.version_info >= (3, 0):
    from urllib.parse import urlencode
else:
    from urllib import urlencode


class QueryParametersSerializer(object):
    @staticmethod
    def serialize(query_parameters):
        # type: (dict) -> str

        for key, value in get_items(query_parameters):
            if isinstance(value, (list, dict)):
                value = json.dumps(value)
            elif isinstance(value, bool):
                value = 'true' if value else 'false'

            query_parameters[key] = value

        return urlencode(
            sorted(get_items(query_parameters), key=lambda val: val[0])
        )


class DataSerializer(object):
    @staticmethod
    def serialize(data):
        # type: (Union[dict, list]) -> str

        return json.dumps(data, cls=JSONEncoder)


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        # type: (object) -> object

        if isinstance(obj, decimal.Decimal):
            return float(obj)
        elif isinstance(obj, datetime.datetime):
            try:
                return int(calendar.timegm(obj.utctimetuple()))
            except ValueError:
                return 0

        try:
            return json.JSONEncoder.default(self, obj)
        except TypeError:
            return str(obj)
