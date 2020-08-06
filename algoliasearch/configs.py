import abc
import os

from typing import Dict, Optional

from algoliasearch.exceptions import AlgoliaException
from algoliasearch.http.hosts import Host, HostsCollection, CallType
from algoliasearch.user_agent import UserAgent


class Config(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, app_id=None, api_key=None):
        # type: (Optional[str], Optional[str]) -> None

        app_id = os.environ["ALGOLIA_APP_ID"] if app_id is None else app_id
        api_key = os.environ["ALGOLIA_API_KEY"] if api_key is None else api_key

        self.app_id = str(app_id)

        assert app_id, "app_id cannot be empty."

        self.api_key = str(api_key)

        # In seconds
        self.read_timeout = 5
        self.write_timeout = 30
        self.connect_timeout = 2

        # In microseconds
        self.wait_task_time_before_retry = 100000

        self.hosts = self.build_hosts()

        self.headers = {
            "X-Algolia-Application-Id": app_id,
            "X-Algolia-API-Key": api_key,
            "User-Agent": UserAgent.get(),
            "Content-Type": "application/json",
        }

        self.proxies = {
            "http": os.environ.get("HTTP_PROXY"),
            "https": os.environ.get("HTTPS_PROXY"),
        }
        if self.proxies["http"] is None:
            del self.proxies["http"]
        if self.proxies["https"] is None:
            del self.proxies["https"]

    @abc.abstractmethod
    def build_hosts(self):
        # type: () -> HostsCollection

        pass  # pragma: no cover


class SearchConfig(Config):
    def __init__(self, app_id=None, api_key=None):
        # type: (Optional[str], Optional[str]) -> None

        super(SearchConfig, self).__init__(app_id, api_key)

        self.batch_size = 1000

    def build_hosts(self):
        # type: () -> HostsCollection

        return HostsCollection(
            [
                Host("{}-dsn.algolia.net".format(self.app_id), 10, CallType.READ),
                Host("{}.algolia.net".format(self.app_id), 10, CallType.WRITE),
                Host("{}-1.algolianet.com".format(self.app_id)),
                Host("{}-2.algolianet.com".format(self.app_id)),
                Host("{}-3.algolianet.com".format(self.app_id)),
            ]
        )


class AnalyticsConfig(Config):
    def __init__(self, app_id=None, api_key=None, region=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> None

        self._region = "us" if region is None else region

        super(AnalyticsConfig, self).__init__(app_id, api_key)

    def build_hosts(self):
        # type: () -> HostsCollection

        return HostsCollection(
            [Host("{}.{}.{}".format("analytics", self._region, "algolia.com"))]
        )


class InsightsConfig(Config):
    def __init__(self, app_id=None, api_key=None, region=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> None

        self._region = "us" if region is None else region

        super(InsightsConfig, self).__init__(app_id, api_key)

    def build_hosts(self):
        # type: () -> HostsCollection

        return HostsCollection(
            [Host("{}.{}.{}".format("insights", self._region, "algolia.io"))]
        )


class RecommendationConfig(Config):
    def __init__(self, app_id=None, api_key=None, region=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> None

        self._region = "us" if region is None else region

        super(RecommendationConfig, self).__init__(app_id, api_key)

    def build_hosts(self):
        # type: () -> HostsCollection

        return HostsCollection(
            [Host("{}.{}.{}".format("recommendation", self._region, "algolia.com"))]
        )
