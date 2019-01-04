from algoliasearch.config.config import Config
from algoliasearch.http.host import Host
from algoliasearch.http.hosts_collection import HostsCollection


class SearchConfig(Config):

    def build_hosts(self):
        # type: () -> HostsCollection

        read_hosts = write_hosts = [
            Host('%s-1.algolianet.com' % self.app_id),
            Host('%s-2.algolianet.com' % self.app_id),
            Host('%s-3.algolianet.com' % self.app_id)
        ]

        read_hosts.append(Host('%s-dsn.algolia.net' % self.app_id, 10))
        write_hosts.append(Host('%s.algolia.net' % self.app_id, 10))

        return HostsCollection(read_hosts, write_hosts)
