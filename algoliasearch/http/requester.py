import requests

from requests import Timeout, RequestException

from algoliasearch.http.transporter import Response, Request


class Requester(object):

    def send(self, request):
        # type: (Request) -> Response

        req = requests.Request(method=request.verb, url=request.url,
                               headers=request.headers,
                               data=request.data_as_string)

        r = req.prepare()  # type: ignore
        s = requests.Session()  # type: ignore

        requests_timeout = (request.connect_timeout, request.timeout)

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
