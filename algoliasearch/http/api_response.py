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
        path: str = "",
        url: str = "",
        status_code: int = None,
        query_parameters: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        data: T = None,
        raw_data: str = None,
        error_message: str = "",
        is_timed_out_error: bool = False,
        is_network_error: bool = False,
        model_config: Dict[str, Any] = {"arbitrary_types_allowed": True},
    ) -> None:
        self.verb = verb
        self.path = path
        self.url = url
        self.status_code = status_code
        self.query_parameters = query_parameters
        self.headers = headers
        self.data = data
        self.raw_data = raw_data
        self.error_message = error_message
        self.is_timed_out_error = is_timed_out_error
        self.is_network_error = is_network_error
        self.model_config = model_config

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
