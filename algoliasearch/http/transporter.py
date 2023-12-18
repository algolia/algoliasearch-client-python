from asyncio import TimeoutError
from json import dumps
from typing import Dict, List, Optional, Tuple, Union
from urllib.parse import urlencode

from aiohttp import ClientSession, TCPConnector
from async_timeout import timeout

from algoliasearch.http.api_response import ApiResponse
from algoliasearch.http.exceptions import (
    AlgoliaUnreachableHostException,
    RequestException,
)
from algoliasearch.http.request_options import RequestOptions
from algoliasearch.http.retry import RetryOutcome, RetryStrategy
from algoliasearch.http.serializer import Serializer
from algoliasearch.http.verb import Verb
from algoliasearch.search.config import Config


class Transporter:
    PRIMITIVE_TYPES = (float, bool, bytes, str, int)

    def __init__(self, config: Config) -> None:
        self._config = config
        self._retry_strategy = RetryStrategy()
        self._serializer = Serializer()

        self._session = ClientSession(
            connector=TCPConnector(use_dns_cache=False), trust_env=True
        )

    async def __aenter__(self) -> None:
        return self

    async def __aexit__(self, exc_type, exc_value, traceback) -> None:
        await self.close()

    async def close(self) -> None:
        if self._session is not None:
            session = self._session
            self._session = None

            await session.close()

    def __enter__(self) -> None:
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        pass

    def sanitize_for_serialization(self, obj) -> dict:
        """Builds a JSON POST object.

        If obj is None, return None.
        If obj is str, int, long, float, bool, return directly.
        If obj is list, sanitize each element in the list.
        If obj is dict, return the dict.
        If obj is OpenAPI model, return the properties dict.

        :param obj: The data to serialize.
        :return: The serialized form of data.
        """
        if obj is None:
            return None
        elif isinstance(obj, self.PRIMITIVE_TYPES):
            return obj
        elif isinstance(obj, list):
            return [self.sanitize_for_serialization(sub_obj) for sub_obj in obj]
        elif isinstance(obj, tuple):
            return tuple(self.sanitize_for_serialization(sub_obj) for sub_obj in obj)
        elif isinstance(obj, dict):
            obj_dict = obj
        else:
            # Convert model obj to dict except
            # attributes `openapi_types`, `attribute_map`
            # and attributes which value is not None.
            # Convert attribute name to json key in
            # model definition for request.
            obj_dict = obj.to_dict()

        return {
            key: self.sanitize_for_serialization(val) for key, val in obj_dict.items()
        }

    def param_serialize(
        self,
        query_params: List[Tuple[str, str]] = [],
        header_params: Dict[str, Optional[str]] = {},
        body: Optional[bytes] = None,
        request_options: Optional[Union[dict, RequestOptions]] = None,
    ) -> Tuple:
        """Builds the HTTP request params needed by the request.
        :param query_params: Query parameters in the url.
        :param body: Request body.
        :param request_options: The request options to send along with the query, they will be merged with the transporter base parameters (headers, query params, timeouts, etc.). (optional)
        :return: tuple of form (body, request_options)
        """

        header_params.update(self._config.headers)

        request_options = RequestOptions.create(
            query_params,
            header_params,
            self._config.read_timeout,
            self._config.write_timeout,
            self._config.connect_timeout,
            request_options,
        )

        if body is not None:
            body = dumps(self.sanitize_for_serialization(body))

        return body, request_options

    async def request(
        self,
        verb: Verb,
        path: str,
        data: Optional[Union[dict, list]],
        request_options: RequestOptions,
        use_read_transporter: bool,
    ) -> ApiResponse:
        query_parameters = dict(request_options.query_parameters)

        if verb == Verb.GET or use_read_transporter:
            self._timeout = request_options.timeouts["read"]
            hosts = self._config.hosts.read()
            query_parameters.update(request_options.data)
        else:
            self._timeout = request_options.timeouts["write"]
            hosts = self._config.hosts.write()

        if isinstance(data, dict):
            data.update(request_options.data)

        if len(query_parameters) > 0:
            path = "{}?{}".format(
                path,
                urlencode(
                    sorted(
                        self._serializer.query_parameters(
                            query_parameters=query_parameters
                        ).items(),
                        key=lambda val: val[0],
                    )
                ),
            )

        for host in self._retry_strategy.valid_hosts(hosts):
            url = "https://{}{}".format(host.url, path)

            proxy = None
            if url.startswith("https"):
                proxy = self._config.proxies.get("https")
            elif url.startswith("http"):
                proxy = self._config.proxies.get("http")

            try:
                async with timeout(self._timeout):
                    resp = await self._session.request(
                        method=verb,
                        url=url,
                        headers=request_options.headers,
                        data=data,
                        proxy=proxy,
                    )

                    response = ApiResponse(
                        verb=verb,
                        url=url,
                        status_code=resp.status,
                        headers=resp.headers,
                        raw_data=await resp.text(),
                        error_message=str(resp.reason),
                    )

            except TimeoutError as e:
                response = ApiResponse(error_message=str(e), is_timed_out_error=True)

            decision = self._retry_strategy.decide(host, response)

            if decision == RetryOutcome.SUCCESS:
                return response
            elif decision == RetryOutcome.FAIL:
                content = response.error_message
                if response.data and "message" in response.data:
                    content = response.content["message"]

                raise RequestException(content, response.status_code)

        raise AlgoliaUnreachableHostException("Unreachable hosts")


class EchoTransporter(Transporter):
    def __init__(self, config: Config) -> None:
        self._config = config
        self._serializer = Serializer()

    async def request(
        self,
        verb: Verb,
        path: str,
        data: Optional[Union[dict, list]],
        request_options: RequestOptions,
        use_read_transporter: bool,
    ) -> ApiResponse:
        return ApiResponse(
            verb=verb,
            path=path,
            status_code=200,
            query_parameters=self._serializer.query_parameters(
                query_parameters=request_options.query_parameters
            ),
            headers=dict(request_options.headers),
            raw_data=data,
        )
