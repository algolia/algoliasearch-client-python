from algoliasearch.config.config import Config
from algoliasearch.http.host import Host
from algoliasearch.http.hosts import Hosts


class SearchConfig(Config):

    def __init__(self, app_id, api_key):
        # type: (str, str) -> None

        Config.__init__(self, app_id, api_key)

        read_hosts = write_hosts = [
            Host('%s-1.algolianet.com' % app_id),
            Host('%s-2.algolianet.com' % app_id),
            Host('%s-3.algolianet.com' % app_id)
        ]

        read_hosts.append(Host('%s-dsn.algolia.net' % app_id, 10))
        write_hosts.append(Host('%s.algolia.net' % app_id, 10))

        self.hosts = Hosts(read_hosts, write_hosts)
