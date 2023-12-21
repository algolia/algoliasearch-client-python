"""API response object."""

from __future__ import annotations

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

    def deserialize(self, klass: any = None) -> T:
        """Deserializes dict, list, str into an object.

        :param data: dict, list or str.
        :param klass: class literal, or string of class name.

        :return: object.
        """
        if self.raw_data is None:
            return None

        if isinstance(klass, str):
            if klass.startswith("List["):
                sub_kls = match(r"List\[(.*)]", klass).group(1)
                return [
                    self.__deserialize(sub_data, sub_kls) for sub_data in self.raw_data
                ]

            if klass.startswith("Dict["):
                sub_kls = match(r"Dict\[([^,]*), (.*)]", klass).group(2)
                return {
                    k: self.__deserialize(v, sub_kls) for k, v in self.raw_data.items()
                }

        if klass in self.PRIMITIVE_TYPES:
            try:
                return klass(self.raw_data)
            except UnicodeEncodeError:
                return str(self.raw_data)
            except TypeError:
                return self.raw_data
        elif klass == object:
            return self.raw_data
        else:
            return klass.from_json(self.raw_data)
