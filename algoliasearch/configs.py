import abc
import os

from typing import Dict, Optional

from algoliasearch.exceptions import AlgoliaException
from algoliasearch.http.hosts import Host, HostsCollection
from algoliasearch.user_agent import UserAgent


class Config(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, app_id=None, api_key=None):
        # type: (Optional[str], Optional[str]) -> None

        app_id = os.environ['ALGOLIA_APP_ID'] if app_id is None else app_id
        api_key = os.environ['ALGOLIA_API_KEY'] if api_key is None else api_key

        self.app_id = str(app_id)

        assert app_id, 'app_id cannot be empty.'

        self.api_key = str(api_key)

        # In seconds
        self.read_timeout = 5
        self.write_timeout = 30
        self.connect_timeout = 2

        # In microseconds
        self.wait_task_time_before_retry = 100000

        self.hosts = self.build_hosts()

        self.headers = {
            'X-Algolia-Application-Id': app_id,
            'X-Algolia-API-Key': api_key,
            'User-Agent': UserAgent.get(),
            'Content-Type': 'application/json',
        }

    @abc.abstractmethod
    def build_hosts(self):
        # type: () -> dict

        pass  # pragma: no cover


class SearchConfig(Config):

    def __init__(self, app_id=None, api_key=None):
        # type: (Optional[str], Optional[str]) -> None

        super(SearchConfig, self).__init__(app_id, api_key)

        self.batch_size = 1000

    def build_hosts(self):
        # type: () -> dict

        read_hosts = write_hosts = [
            Host('{}-1.algolianet.com'.format(self.app_id)),
            Host('{}-2.algolianet.com'.format(self.app_id)),
            Host('{}-3.algolianet.com'.format(self.app_id))
        ]

        read_hosts.append(Host('{}-dsn.algolia.net'.format(self.app_id, 10)))
        write_hosts.append(Host('{}.algolia.net'.format(self.app_id, 10)))

        return {
            'read': HostsCollection(read_hosts),
            'write': HostsCollection(write_hosts)
        }


class AnalyticsConfig(Config):

    def __init__(self, app_id=None, api_key=None, region=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> None

        self.__region = 'us' if region is None else region

        super(AnalyticsConfig, self).__init__(app_id, api_key)

    def build_hosts(self):
        # type: () -> Dict[str, HostsCollection]

        read_hosts = write_hosts = [
            Host('{}.{}.{}'.format('analytics', self.__region, 'algolia.com'))
        ]

        return {
            'read': HostsCollection(read_hosts),
            'write': HostsCollection(write_hosts)
        }


class InsightsConfig(Config):

    def __init__(self, app_id=None, api_key=None, region=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> None

        self.__region = 'us' if region is None else region

        super(InsightsConfig, self).__init__(app_id, api_key)

    def build_hosts(self):
        # type: () -> dict

        read_hosts = write_hosts = [
            Host('{}.{}.{}'.format('insights', self.__region, 'algolia.io'))
        ]

        return {
            'read': HostsCollection(read_hosts),
            'write': HostsCollection(write_hosts)
        }
