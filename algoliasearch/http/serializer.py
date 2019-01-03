import json
import calendar
import datetime
import decimal


class Serializer(object):
    @staticmethod
    def serialize(data):
        # type: (dict) -> str

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
