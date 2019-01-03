import requests
import json

from algoliasearch.http.serializer import Serializer


class Requester(object):
    def request(self, verb, url, headers, data):
        if data is not None:
            data = Serializer.serialize(data)

        req = requests.Request(method=verb, url=url, headers=headers,
                               data=data)
        r = req.prepare()

        s = requests.Session()

        response = s.send(r)

        return None if response.content is None else json.loads(
            response.content.decode('utf-8'))
