from copy import deepcopy
from sys import version_info
from typing import Any, Dict, Optional, Union
from urllib.parse import quote

from algoliasearch.http.base_config import BaseConfig
from algoliasearch.http.serializer import QueryParametersSerializer

if version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


class RequestOptions:
    def __init__(
        self,
        config: BaseConfig,
        headers: Optional[Dict[str, str]] = None,
        query_parameters: Optional[Dict[str, Any]] = None,
        timeouts: Optional[Dict[str, int]] = None,
        data: Optional[Dict[str, Any]] = None,
    ) -> None:
        if headers is None:
            headers = {}
        if query_parameters is None:
            query_parameters = {}
        if timeouts is None:
            timeouts = {}
        self._config = config
        self.headers = headers
        self.query_parameters = {
            quote(k): quote(v)
            for k, v in QueryParametersSerializer(
                query_parameters
            ).query_parameters.items()
        }
        self.timeouts = timeouts
        self.data = data

    def to_dict(self) -> Dict[str, Any]:
        return deepcopy(self.__dict__)

    def to_json(self) -> str:
        return str(self.__dict__)

    def from_dict(self, data: Dict[str, Dict[str, Any]]) -> Self:
        return RequestOptions(
            config=self._config,
            headers=data.get("headers", {}),
            query_parameters=data.get("query_parameters", {}),
            timeouts=data.get("timeouts", {}),
            data=data.get("data", {}),
        )  # pyright: ignore

    def merge(
        self,
        query_parameters: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        data: Optional[str] = None,
        timeouts: Dict[str, int] = {},
        user_request_options: Optional[Union[Self, Dict[str, Any]]] = None,
    ) -> Self:
        """
        Merges the default config values with the user given request options if it exists.
        """

        if query_parameters is None:
            query_parameters = {}
        if headers is None:
            headers = {}
        headers.update(self._config.headers)

        request_options = {
            "headers": headers,
            "query_parameters": query_parameters,
            "timeouts": {
                "read": timeouts.get("read", self._config.read_timeout),
                "write": timeouts.get("write", self._config.write_timeout),
                "connect": timeouts.get("connect", self._config.connect_timeout),
            },
            "data": data,
        }

        if user_request_options is not None:
            if isinstance(user_request_options, RequestOptions):
                _user_request_options = user_request_options.to_dict()
            else:
                _user_request_options = user_request_options

            for key, value in _user_request_options.items():
                if request_options[key] is None:
                    request_options[key] = value
                else:
                    request_options[key].update(value)

        return self.from_dict(request_options)
