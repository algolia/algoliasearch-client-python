"""API response object."""

from __future__ import annotations

import json
from re import match
from typing import Any, Dict, Generic, Optional, TypeVar

from algoliasearch.http.verb import Verb

T = TypeVar("T")

PRIMITIVE_TYPES = (float, bool, bytes, str, int)


class ApiResponse(Generic[T]):
    """
    API response object
    """

    def __init__(
        self,
        verb: Verb,
        data: Optional[T] = None,
        error_message: str = "",
        headers: Optional[Dict[str, str]] = None,
        host: str = "",
        is_network_error: bool = False,
        is_timed_out_error: bool = False,
        path: str = "",
        query_parameters: Optional[Dict[str, Any]] = None,
        raw_data: Optional[str] = None,
        status_code: Optional[int] = None,
        timeouts: Optional[Dict[str, int]] = None,
        url: str = "",
    ) -> None:
        self.verb = verb
        self.data = data
        self.error_message = error_message
        self.headers = headers
        self.host = host
        self.is_network_error = is_network_error
        self.is_timed_out_error = is_timed_out_error
        self.path = path
        self.query_parameters = query_parameters
        self.raw_data = raw_data
        self.status_code = status_code
        self.timeouts = timeouts
        self.url = url

    def to_json(self) -> str:
        return str(self.__dict__)

    @staticmethod
    def deserialize(klass: Any = None, data: Any = None) -> Any:
        """Deserializes dict, list, str into an object.

        :param data: dict, list or str.
        :param klass: class literal, or string of class name.

        :return: object.
        """
        if data is None:
            return None

        if hasattr(klass, "__origin__") and klass.__origin__ is list:
            sub_kls = klass.__args__[0]
            arr = json.loads(data)
            return [ApiResponse.deserialize(sub_kls, sub_data) for sub_data in arr]

        if isinstance(klass, str):
            if klass.startswith("List["):
                sub_kls = match(r"List\[(.*)]", klass)
                if sub_kls is not None:
                    sub_kls = sub_kls.group(1)
                return [ApiResponse.deserialize(sub_kls, sub_data) for sub_data in data]

            if klass.startswith("Dict["):
                sub_kls = match(r"Dict\[([^,]*), (.*)]", klass)
                if sub_kls is not None:
                    sub_kls = sub_kls.group(2)
                return {k: ApiResponse.deserialize(sub_kls, v) for k, v in data.items()}

        if klass in PRIMITIVE_TYPES:
            try:
                return klass(data)
            except UnicodeEncodeError:
                return str(data)
            except TypeError:
                return data
        if klass is object:
            if isinstance(data, str):
                return json.loads(data)
            return data

        if isinstance(data, str):
            return klass.from_json(data)  # pyright: ignore

        return klass.from_dict(data)  # pyright: ignore
