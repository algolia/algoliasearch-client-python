import asyncio
import aiohttp

from typing import Optional, Union

from algoliasearch.http.serializer import DataSerializer
from algoliasearch.http.transporter import Response


class RequesterAsync(object):

    @asyncio.coroutine
    def request(self, verb, url, headers, data, timeout, connect_timeout):
        # type: (str, str, dict, Optional[Union[dict, list]], int, int) -> Response  # noqa: E501

        connector = aiohttp.TCPConnector(use_dns_cache=False)

        data_as_string = '' if data is None else DataSerializer.serialize(data)

        session = aiohttp.ClientSession(connector=connector,
                                        timeout=connect_timeout)

        request = session.request(
            method=verb, url=url,
            headers=headers,
            data=data_as_string,
            timeout=timeout,
        )

        try:
            response = yield from request
            json = yield from response.json()
        except asyncio.TimeoutError as e:
            return Response(error_message=str(e),
                            is_timed_out_error=True)
        # @todo Check if there is an Request Exception here.
        finally:
            yield from session.close()

        return Response(
            response.status,
            json,
            response.reason
        )
