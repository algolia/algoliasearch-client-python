from algoliasearch.http.request_options import RequestOptions
from algoliasearch.config.config import Config
from algoliasearch.http.requester import Requester

import sys

if sys.version_info >= (3, 0):
    from urllib.parse import urlencode
else:
    from urllib import urlencode


class Transporter(object):
    def __init__(self, requester, config):
        # type: (Requester, Config) -> None

        self.__requester = requester
        self.__config = config

    def write(self, verb, path, data, request_options):
        # type: (str, str, dict, RequestOptions) -> dict

        return self.__request(verb, self.__config.hosts.write, path, data,
                              request_options)

    def read(self, verb, path, request_options):
        # type: (str, str, RequestOptions) -> dict

        return self.__request(verb, self.__config.hosts.read, path, {},
                              request_options)

    def __request(self, verb, hosts, path, data, request_options):
        # type: (str, list, str, dict, RequestOptions) -> dict

        host = hosts[1]
        url = 'https://%s/%s%s' % (
            host.url, path, urlencode(request_options.query_parameters))

        return self.__requester.request(verb, url, request_options.headers,
                                        data)
