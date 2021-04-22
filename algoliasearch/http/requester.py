from typing import Union

import requests

from requests import Timeout, RequestException, Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util import Retry

from algoliasearch.http.transporter import Response, Request


class Requester(object):
    def __init__(self):
        # type: () -> None

        self._session = None  # type: Union[None, Session]

    def send(self, request):
        # type: (Request) -> Response

        if self._session is None:
            self._session = requests.Session()

            # Ask urllib not to make retries on its own.
            self._session.mount("https://", HTTPAdapter(max_retries=Retry(connect=0)))

        req = requests.Request(
            method=request.verb,
            url=request.url,
            headers=request.headers,
            data=request.data_as_string,
        )

        r = req.prepare()  # type: ignore

        requests_timeout = (request.connect_timeout, request.timeout)

        try:
            response = self._session.send(  # type: ignore
                r, timeout=requests_timeout, proxies=request.proxies,
            )
        except Timeout as e:
            return Response(error_message=str(e), is_timed_out_error=True)
        except RequestException as e:
            return Response(error_message=str(e), is_network_error=True)

        return Response(response.status_code, response.json(), response.reason)

    def close(self):
        # type: () -> None

        if self._session is not None:
            self._session.close()
            self._session = None
