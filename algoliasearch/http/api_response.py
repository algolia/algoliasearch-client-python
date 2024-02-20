"""API response object."""

from __future__ import annotations

import json
from re import match
from typing import Any, Dict, Generic, Optional, TypeVar

from algoliasearch.http.verb import Verb

T = TypeVar("T")


class ApiResponse(Generic[T]):
    """
    API response object
    """

    PRIMITIVE_TYPES = (float, bool, bytes, str, int)

    def __init__(
        self,
        verb: Verb,
        data: T = None,
        error_message: str = "",
        headers: Optional[Dict[str, str]] = None,
        host: str = "",
        is_network_error: bool = False,
        is_timed_out_error: bool = False,
        path: str = "",
        query_parameters: Optional[Dict[str, Any]] = None,
        raw_data: str = None,
        status_code: int = None,
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

    def deserialize(self, klass: any = None, data: any = None) -> T:
        """Deserializes dict, list, str into an object.

        :param data: dict, list or str.
        :param klass: class literal, or string of class name.

        :return: object.
        """
        if data is None:
            data = self.raw_data
        if data is None:
            return None

        if hasattr(klass, "__origin__") and klass.__origin__ is list:
            sub_kls = klass.__args__[0]
            arr = json.loads(data)
            return [self.deserialize(sub_kls, sub_data) for sub_data in arr]

        if isinstance(klass, str):
            if klass.startswith("List["):
                sub_kls = match(r"List\[(.*)]", klass).group(1)
                return [self.deserialize(sub_kls, sub_data) for sub_data in data]

            if klass.startswith("Dict["):
                sub_kls = match(r"Dict\[([^,]*), (.*)]", klass).group(2)
                return {k: self.deserialize(sub_kls, v) for k, v in data.items()}

        if klass in self.PRIMITIVE_TYPES:
            try:
                return klass(data)
            except UnicodeEncodeError:
                return str(data)
            except TypeError:
                return data
        if klass == object:
            return data

        if isinstance(data, str):
            return klass.from_json(data)

        return klass.from_dict(data)
