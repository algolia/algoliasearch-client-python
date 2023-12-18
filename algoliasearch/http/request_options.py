from copy import deepcopy
from typing import Any, Dict, List, Optional, Tuple, Union

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
        query_params: List[Tuple[str, str]],
        header_params: Dict[str, Optional[str]],
        default_read_timeout: int,
        default_write_timeout: int,
        default_connect_timeout: int,
        user_request_options: Optional[Union[Self, Dict[str, Any]]] = None,
    ) -> Self:
        """
        Overrides the default config values with the user given request options if it exists, merges it if not.
        """

        request_options = {
            "headers": header_params,
            "query_parameters": {k: v for k, v in query_params},
            "timeouts": {
                "read": default_read_timeout,
                "write": default_write_timeout,
                "connect": default_connect_timeout,
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
