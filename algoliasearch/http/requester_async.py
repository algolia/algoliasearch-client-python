import asyncio
import types

import aiohttp
import async_timeout

from algoliasearch.http.requester import Requester
from algoliasearch.http.transporter import Response, Request


class RequesterAsync(Requester):

    def __init__(self):
        # type: () -> None

        self.__session = None

    @asyncio.coroutine  # type: ignore
    def send(self, request):  # type: ignore
        # type: (Request) -> Response

        if self.__session is None:
            connector = aiohttp.TCPConnector(use_dns_cache=False)
            self.__session = aiohttp.ClientSession(  # type: ignore
                connector=connector)

        try:
            with async_timeout.timeout(request.timeout):
                response = yield from (self.__session.request(  # type: ignore
                    method=request.verb, url=request.url,
                    headers=request.headers,
                    data=request.data_as_string
                ))

                json = yield from response.json()

        except asyncio.TimeoutError as e:

            return Response(
                error_message=str(e),
                is_timed_out_error=True
            )

        return Response(
            response.status,
            json,
            str(response.reason)
        )

    @asyncio.coroutine  # type: ignore
    def close(self):
        # type: () -> None

        if self.__session is not None and not self.__session.closed:
            yield from self.__session.close()
