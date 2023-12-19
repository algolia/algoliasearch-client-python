from copy import deepcopy
from typing import Any, Dict, List, Optional, Tuple, Union

from algoliasearch.http.base_config import BaseConfig

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class RequestOptions:
    def __init__(
        self,
        headers: Dict[str, str],
        query_parameters: Dict[str, Any],
        timeouts: Dict[str, int],
        data: Dict[str, Any],
    ) -> None:
        self.headers = headers
        self.query_parameters = query_parameters
        self.timeouts = timeouts
        self.data = data

    def to_dict(self) -> Dict[str, Any]:
        return deepcopy(self.__dict__)

    def to_json(self) -> str:
        return str(self.__dict__)

    def from_dict(data: Optional[Dict[str, Dict[str, Any]]]) -> Self:
        return RequestOptions(
            data.get("headers", {}),
            data.get("query_parameters", {}),
            data.get("timeouts", {}),
            data.get("data", {}),
        )

    def create(
        config: BaseConfig,
        query_parameters: List[Tuple[str, str]] = [],
        headers_parameters: Dict[str, Optional[str]] = {},
        user_request_options: Optional[Union[Self, Dict[str, Any]]] = None,
    ) -> Self:
        """
        Overrides the default config values with the user given request options if it exists, merges it if not.
        """

        headers_parameters.update(config.headers)

        request_options = {
            "headers": headers_parameters,
            "query_parameters": {k: v for k, v in query_parameters},
            "timeouts": {
                "read": config.read_timeout,
                "write": config.write_timeout,
                "connect": config.connect_timeout,
            },
            "data": {},
        }

        if user_request_options is not None:
            if isinstance(user_request_options, RequestOptions):
                _user_request_options = user_request_options.to_dict()
            else:
                _user_request_options = user_request_options

            for key, value in _user_request_options.items():
                request_options[key].update(value)

        return RequestOptions.from_dict(request_options)
