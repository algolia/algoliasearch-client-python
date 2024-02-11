from json import dumps
from typing import Any, Dict

PRIMITIVE_TYPES = (float, bool, bytes, str, int)


class QueryParametersSerializer:
    """
    Parses the given 'query_parameters' values of each keys into their string value.
    """

    query_parameters: Dict[str, Any] = {}

    def parse(self, value) -> Any:
        if isinstance(value, dict):
            return dumps(value)
        elif isinstance(value, list):
            return ",".join([self.parse(item) for item in value])
        elif isinstance(value, bool):
            return "true" if value else "false"
        else:
            return str(value)

    def __init__(self, query_parameters: Dict[str, Any]) -> None:
        self.query_parameters = {}
        for key, value in query_parameters.items():
            self.query_parameters[key] = self.parse(value)


def bodySerializer(obj: Any) -> dict:
    """Builds a JSON POST object.

    If obj is None, return None.
    If obj is str, int, long, float, bool, return directly.
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
    elif isinstance(obj, list):
        return [bodySerializer(sub_obj) for sub_obj in obj]
    elif isinstance(obj, tuple):
        return tuple(bodySerializer(sub_obj) for sub_obj in obj)
    elif isinstance(obj, dict):
        obj_dict = obj
    else:
        obj_dict = obj.to_dict()
        if obj_dict is None:
            return None

    return {key: bodySerializer(val) for key, val in obj_dict.items()}
