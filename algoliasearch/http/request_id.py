from copy import copy
from secrets import token_bytes
from typing import Any, Dict, Optional, TypeVar, Union, cast

from algoliasearch.http.base_config import BaseConfig
from algoliasearch.http.request_options import RequestOptions

REQUEST_ID_HEADER = "request-id"
REQUEST_ID_QUERY_PARAMETER = "x-algolia-request-id"
CORRELATION_ID_HEADER = "correlation-id"

REQUEST_ID_ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
REQUEST_ID_LENGTH = 11

RequestOptionsType = TypeVar(
    "RequestOptionsType", bound=Optional[Union[dict, RequestOptions]]
)


def generate_request_id() -> str:
    """Returns a fresh 11 character base62 identifier for the Request-ID header."""
    return "".join(
        REQUEST_ID_ALPHABET[byte % len(REQUEST_ID_ALPHABET)]
        for byte in token_bytes(REQUEST_ID_LENGTH)
    )


def _contains_key(mapping: Optional[Dict[str, Any]], name: str) -> bool:
    if not mapping:
        return False

    return any(str(key).lower() == name for key in mapping)


def has_request_id(headers: Optional[Dict[str, Any]]) -> bool:
    """Whether the headers already carry a Request-ID entry, whatever its casing."""
    return _contains_key(headers, REQUEST_ID_HEADER)


def has_request_id_query_parameter(query_parameters: Optional[Dict[str, Any]]) -> bool:
    """Whether the query parameters already carry an x-algolia-request-id entry, whatever its casing."""
    return _contains_key(query_parameters, REQUEST_ID_QUERY_PARAMETER)


def get_correlation_id(headers: Optional[Dict[str, Any]]) -> Optional[str]:
    """Reads the Correlation-ID response header, whatever its casing."""
    if not headers:
        return None

    for key, value in headers.items():
        if str(key).lower() == CORRELATION_ID_HEADER:
            return value

    return None


def with_request_id(
    request_options: RequestOptionsType, config: BaseConfig
) -> RequestOptionsType:
    """
    Derives the request options carrying the Request-ID shared by every request of one
    invocation. The given options are never modified, so a caller reusing one object across
    calls still gets a fresh id per call. Returns them untouched when the client does not
    support Request-ID, or when the caller already supplied one on either channel.
    """
    if not config.request_id_enabled:
        return request_options

    given: Any = request_options
    is_request_options = isinstance(given, RequestOptions)

    headers = given.headers if is_request_options else (given or {}).get("headers")
    query_parameters = (
        given.query_parameters
        if is_request_options
        else (given or {}).get("query_parameters")
    )

    if (
        has_request_id(headers)
        or has_request_id_query_parameter(query_parameters)
        or has_request_id(config.headers)
    ):
        return request_options

    request_id_headers = {**(headers or {}), REQUEST_ID_HEADER: generate_request_id()}

    options: Any
    if is_request_options:
        options = copy(given)
        options.headers = request_id_headers
    else:
        options = dict(given or {})
        options["headers"] = request_id_headers

    return cast(RequestOptionsType, options)
