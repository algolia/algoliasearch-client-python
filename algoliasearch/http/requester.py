import requests

from requests import Timeout
from typing import Optional

from algoliasearch.http.serializer import Serializer
from algoliasearch.http.transporter import Response


class Requester(object):

    def request(self, verb, url, headers, data, timeout, connect_timeout):
        # type: (str, str, dict, Optional[dict], int, int) -> Response

        data_as_string = '' if data is None else Serializer.serialize(data)

        req = requests.Request(method=verb, url=url, headers=headers,
                               data=data_as_string)
        r = req.prepare()  # type: ignore

        s = requests.Session()  # type: ignore

        requests_timeout = (connect_timeout, timeout)

        try:
            response = s.send(r, timeout=requests_timeout)  # type: ignore
            s.close()
        except Timeout as e:
            return Response(error_message=str(e), timed_out=True)

        return Response(
            response.status_code,
            response.json(),
            response.reason
        )
