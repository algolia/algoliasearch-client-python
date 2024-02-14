from os import environ
from typing import Optional

from algoliasearch.http.base_config import BaseConfig
from algoliasearch.http.hosts import CallType, Host, HostsCollection
from algoliasearch.http.user_agent import UserAgent


class RecommendConfig(BaseConfig):
    def __init__(
        self, app_id: Optional[str] = None, api_key: Optional[str] = None
    ) -> None:
        super().__init__(app_id, api_key)

        user_agent = UserAgent().add("Recommend")

        self.headers = {
            "x-algolia-application-id": app_id,
            "x-algolia-api-key": api_key,
            "user-agent": user_agent.get(),
            "content-type": "application/json",
        }

        self.proxies = {
            "http": environ.get("HTTP_PROXY"),
            "https": environ.get("HTTPS_PROXY"),
        }
        if self.proxies["http"] is None:
            del self.proxies["http"]
        if self.proxies["https"] is None:
            del self.proxies["https"]

        self.hosts = HostsCollection(
            [
                Host(
                    url="{}-dsn.algolia.net".format(self.app_id),
                    priority=10,
                    accept=CallType.READ,
                ),
                Host(
                    url="{}.algolia.net".format(self.app_id),
                    priority=10,
                    accept=CallType.WRITE,
                ),
                Host("{}-1.algolianet.com".format(self.app_id)),
                Host("{}-2.algolianet.com".format(self.app_id)),
                Host("{}-3.algolianet.com".format(self.app_id)),
            ],
            reorder_hosts=True,
        )
