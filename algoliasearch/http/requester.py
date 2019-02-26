import requests

from requests import Timeout, RequestException, HTTPError
from typing import Optional, Union

from algoliasearch.http.serializer import DataSerializer
from algoliasearch.http.transporter import Response


class Requester(object):

    def request(self, verb, url, headers, data, timeout, connect_timeout):
        # type: (str, str, dict, Optional[Union[dict, list]], int, int) -> Response  # noqa: E501

        data_as_string = '' if data is None else DataSerializer.serialize(data)

        req = requests.Request(method=verb, url=url, headers=headers,
                               data=data_as_string)

        r = req.prepare()  # type: ignore
        s = requests.Session()  # type: ignore

        requests_timeout = (connect_timeout, timeout)

        try:
            response = s.send(r, timeout=requests_timeout)  # type: ignore
        except Timeout as e:
            return Response(error_message=str(e), is_timed_out_error=True)
        except RequestException as e:
            return Response(error_message=str(e), is_network_error=True)
        finally:
            s.close()

        return Response(
            response.status_code,
            response.json(),
            response.reason
        )
