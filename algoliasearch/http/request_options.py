from copy import deepcopy
from typing import Any, Dict, List, Optional, Tuple, Union
from urllib.parse import quote

from algoliasearch.http.base_config import BaseConfig
from algoliasearch.http.serializer import QueryParametersSerializer

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class RequestOptions:
    _config: BaseConfig
    headers: Dict[str, str]
    query_parameters: Dict[str, Any]
    timeouts: Dict[str, int]
    data: Dict[str, Any]

    def __init__(
        self,
        config: BaseConfig,
        headers: Dict[str, str] = {},
        query_parameters: Dict[str, Any] = {},
        timeouts: Dict[str, int] = {},
        data: Dict[str, Any] = {},
    ) -> None:
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

    def from_dict(self, data: Optional[Dict[str, Dict[str, Any]]]) -> Self:
        return RequestOptions(
            config=self._config,
            headers=data.get("headers", {}),
            query_parameters=data.get("query_parameters", {}),
            timeouts=data.get("timeouts", {}),
            data=data.get("data", {}),
        )

    def merge(
        self,
        query_parameters: List[Tuple[str, str]] = [],
        headers: Dict[str, Optional[str]] = {},
        timeouts: Dict[str, int] = {},
        data: Optional[Union[dict, list]] = None,
        user_request_options: Optional[Union[Self, Dict[str, Any]]] = None,
    ) -> Self:
        """
        Merges the default config values with the user given request options if it exists.
        """

        headers.update(self._config.headers)

        request_options = {
            "headers": headers,
            "query_parameters": {k: v for k, v in query_parameters},
            "timeouts": {
                "read": self._config.read_timeout,
                "write": self._config.write_timeout,
                "connect": self._config.connect_timeout,
            },
            "data": data,
        }

        if user_request_options is not None:
            if isinstance(user_request_options, RequestOptions):
                _user_request_options = user_request_options.to_dict()
            else:
                _user_request_options = user_request_options

            for key, value in _user_request_options.items():
                if key == "data" and isinstance(value, dict):
                    request_options.data = value
                    continue
                request_options[key].update(value)

        return self.from_dict(request_options)
