from copy import deepcopy
from typing import Any, Dict, Optional, Union

from algoliasearch.search.config import Config

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
        config: Config,
        user_request_options: Optional[Union[Self, Dict[str, Any]]] = None,
    ) -> Self:
        """
        Creates a RequestOption object from the given `options`, then merges
        it with the given configuration, overriding the already
        existing `config` options.
        """

        request_options = {
            "headers": dict(config.headers),
            "query_parameters": {},
            "timeouts": {
                "readTimeout": int(config.read_timeout),
                "writeTimeout": int(config.write_timeout),
                "connectTimeout": int(config.connect_timeout),
            },
            "data": {},
        }

        if user_request_options is not None:
            if isinstance(user_request_options, RequestOptions):
                _user_request_options = user_request_options.to_dict()
            else:
                _user_request_options = user_request_options or {}

            for key, value in _user_request_options.items():
                if value is not None:
                    request_options[key].update(value)

        return RequestOptions.from_dict(request_options)
