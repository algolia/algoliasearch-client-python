"""API response object."""

from __future__ import annotations

from typing import Any, Dict, Generic, Optional, TypeVar

T = TypeVar("T")


class ApiResponse(Generic[T]):
    """
    API response object
    """

    def __init__(
        self,
        url: str = "",
        status_code: int = None,
        headers: Optional[Dict[str, str]] = None,
        data: T = None,
        raw_data: str = None,
        error_message: str = "",
        is_timed_out_error: bool = False,
        is_network_error: bool = False,
        model_config: Dict[str, Any] = {"arbitrary_types_allowed": True},
    ) -> None:
        self.url = url
        self.status_code = status_code
        self.headers = headers
        self.data = data
        self.raw_data = raw_data
        self.error_message = error_message
        self.is_timed_out_error = is_timed_out_error
        self.is_network_error = is_network_error
        self.model_config = model_config
