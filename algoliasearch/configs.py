import abc

from algoliasearch.http.hosts import Host, HostsCollection


class Config(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, app_id, api_key):
        # type: (str, str) -> None

        self.app_id = app_id
        self.api_key = api_key

        # In seconds
        self.read_timeout = 5
        self.write_timeout = 5

        # In microseconds
        self.wait_task_time_before_retry = 100000

        self.hosts = self.build_hosts()

    @abc.abstractmethod
    def build_hosts(self):
        # type: () -> dict

        pass


class SearchConfig(Config):

    def build_hosts(self):
        # type: () -> dict

        read_hosts = write_hosts = [
            Host('%s-1.algolianet.com' % self.app_id),
            Host('%s-2.algolianet.com' % self.app_id),
            Host('%s-3.algolianet.com' % self.app_id)
        ]

        read_hosts.append(Host('%s-dsn.algolia.net' % self.app_id, 10))
        write_hosts.append(Host('%s.algolia.net' % self.app_id, 10))

        return {
            'read': HostsCollection(read_hosts),
            'write': HostsCollection(write_hosts)
        }
