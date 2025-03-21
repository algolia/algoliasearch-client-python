from decimal import Decimal
from json import dumps
from typing import Any, Dict, Optional
from urllib.parse import urlencode

PRIMITIVE_TYPES = (float, bool, bytes, str, int)


class QueryParametersSerializer:
    """
    Parses the given 'query_parameters' values of each keys into their string value.
    """

    def __init__(self, query_parameters: Optional[Dict[str, Any]]) -> None:
        self.query_parameters: Dict[str, Any] = {}
        if query_parameters is None:
            return
        for key, value in query_parameters.items():
            if isinstance(value, dict):
                for dkey, dvalue in value.items():
                    self.query_parameters[dkey] = self.parse(dvalue)
            else:
                self.query_parameters[key] = self.parse(value)

    def parse(self, value) -> Any:
        if isinstance(value, list):
            return ",".join([self.parse(item) for item in value])
        elif isinstance(value, dict):
            return dumps(value)
        elif isinstance(value, bool):
            return "true" if value else "false"
        else:
            return str(value)

    def encoded(self) -> str:
        return urlencode(
            dict(sorted(self.query_parameters.items(), key=lambda val: val[0]))
        ).replace("+", "%20")


def body_serializer(obj: Any) -> Any:
    """Builds a JSON POST object.

    If obj is None, return None.
    If obj is str, int, long, float, bool, return directly.
    If obj is Decimal, convert to float and return.
    If obj is list, sanitize each element in the list.
    If obj is dict, return the dict.
    If obj is OpenAPI model, return the properties dict.

    :param obj: The data to serialize.
    :return: The serialized form of data.
    """

    if obj is None:
        return None
    elif isinstance(obj, PRIMITIVE_TYPES):
        return obj
    elif isinstance(obj, Decimal):
        return float(obj)
    elif isinstance(obj, list):
        return [body_serializer(sub_obj) for sub_obj in obj]
    elif isinstance(obj, tuple):
        return tuple(body_serializer(sub_obj) for sub_obj in obj)
    elif isinstance(obj, dict):
        obj_dict = obj
    else:
        obj_dict = obj.to_dict()
        if obj_dict is None:
            return None

    return {key: body_serializer(val) for key, val in obj_dict.items()}
