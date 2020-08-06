import asyncio

import aiohttp
import async_timeout

from algoliasearch.http.requester import Requester
from algoliasearch.http.transporter import Response, Request


class RequesterAsync(Requester):
    def __init__(self):
        # type: () -> None

        self._session = None

    @asyncio.coroutine  # type: ignore
    def send(self, request):  # type: ignore
        # type: (Request) -> Response

        if self._session is None:
            connector = aiohttp.TCPConnector(use_dns_cache=False)
            self._session = aiohttp.ClientSession(  # type: ignore
                connector=connector
            )

        proxy = None
        if request.url.startswith("https"):
            proxy = request.proxies.get("https")
        elif request.url.startswith("http"):
            proxy = request.proxies.get("http")

        try:
            with async_timeout.timeout(request.timeout):
                response = yield from (
                    self._session.request(  # type: ignore
                        method=request.verb,
                        url=request.url,
                        headers=request.headers,
                        data=request.data_as_string,
                        proxy=proxy,
                    )
                )

                json = yield from response.json()

        except asyncio.TimeoutError as e:

            return Response(error_message=str(e), is_timed_out_error=True)

        return Response(response.status, json, str(response.reason))

    @asyncio.coroutine
    def close(self):  # type: ignore
        # type: () -> None

        if self._session is not None:
            session = self._session
            self._session = None

            yield from session.close()  # type: ignore
