from ..http.hosts import Hosts
from ..http.host import Host

class Config(object):
    def __init__(self, app_id, api_key):
        # type: (str, str) -> None

        self.app_id = app_id
        self.api_key = api_key
        self.hosts = self.__create_from_app_id(app_id)
        self.read_timeout = 5
        self.write_timeout = 5
        self.connect_timeout = 5

    def __create_from_app_id(self, app_id):
        # type: (str) -> Hosts

        read_hosts = write_hosts = [
            Host('%s-1.algolianet.com' % app_id),
            Host('%s-2.algolianet.com' % app_id),
            Host('%s-3.algolianet.com' % app_id)
        ]

        read_hosts.append(Host('%s-dsn.algolia.net' % app_id, 10))
        write_hosts.append(Host('%s.algolia.net' % app_id, 10))

        return Hosts(read_hosts, write_hosts)
