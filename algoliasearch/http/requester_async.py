import asyncio
import aiohttp
import async_timeout

from algoliasearch.http.requester import Requester
from algoliasearch.http.transporter import Response, Request


class RequesterAsync(Requester):

    @asyncio.coroutine  # type: ignore
    def send(self, request):  # type: ignore
        # type: (Request) -> Response

        connector = aiohttp.TCPConnector(use_dns_cache=False)

        session = aiohttp.ClientSession(connector=connector,
                                        conn_timeout=request.connect_timeout)

        try:
            with async_timeout.timeout(request.timeout):
                response = yield from (session.request(  # type: ignore
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
        finally:
            yield from session.close()

        return Response(
            response.status,
            json,
            str(response.reason)
        )
