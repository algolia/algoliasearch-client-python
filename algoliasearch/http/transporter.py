from algoliasearch.http.requester import Requester


class Transporter(object):
    def __init__(self, requester: Requester, config):
        self.__requester = requester
        self.__config = config

    def write(self, verb: str, path: str, payload: dict, request_options):
        return self.__request(verb, self.__config.hosts.write, path, payload, request_options)

    def read(self, verb: str, path: str, request_options):
        return self.__request(verb, self.__config.hosts.read, path, {}, request_options)

    # Todo retry strategy
    def __request(self, verb: str, hosts: dict, path: str, payload: dict, request_options):
        host = hosts[1]
        url = "%s/%s" % (host.url, path)
        self.__requester.request(verb, url, payload, request_options)
