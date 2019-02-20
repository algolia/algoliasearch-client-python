import abc
from platform import python_version

from algoliasearch.http.hosts import Host, HostsCollection
from algoliasearch.version import VERSION


class Config(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, app_id, api_key):
        # type: (str, str) -> None

        self.app_id = app_id
        self.api_key = api_key

        # In seconds
        self.read_timeout = 5
        self.write_timeout = 30
        self.connect_timeout = 2

        # In microseconds
        self.wait_task_time_before_retry = 100000

        self.hosts = self.build_hosts()

        python_version_str = str(python_version())  # type: ignore

        self.headers = {
            'X-Algolia-Application-Id': app_id,
            'X-Algolia-API-Key': api_key,
            'User-Agent': 'Algolia for Python (%s); Python (%s)' % (
                VERSION, python_version_str),
            'Content-Type': 'application/json',
        }

    @abc.abstractmethod
    def build_hosts(self):
        # type: () -> dict

        pass  # pragma: no cover


class SearchConfig(Config):

    def __init__(self, app_id, api_key):
        # type: (str, str) -> None

        super(SearchConfig, self).__init__(app_id, api_key)

        self.batch_size = 1000

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


class AnalyticsConfig(Config):

    def __init__(self, app_id, api_key, region):
        # type: (str, str, str) -> None

        self.__region = region

        super(AnalyticsConfig, self).__init__(app_id, api_key)

    def build_hosts(self):
        # type: () -> dict

        read_hosts = write_hosts = [
            Host('analytics.' + self.__region + '.algolia.com')
        ]

        return {
            'read': HostsCollection(read_hosts),
            'write': HostsCollection(write_hosts)
        }


class InsightsConfig(Config):

    def __init__(self, app_id, api_key, region):
        # type: (str, str, str) -> None

        self.__region = region

        super(InsightsConfig, self).__init__(app_id, api_key)

    def build_hosts(self):
        # type: () -> dict

        read_hosts = write_hosts = [
            Host('insights.' + self.__region + '.algolia.io')
        ]

        return {
            'read': HostsCollection(read_hosts),
            'write': HostsCollection(write_hosts)
        }
