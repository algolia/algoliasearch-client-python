from os import environ

from algoliasearch.http.base_config import BaseConfig
from algoliasearch.http.hosts import CallType, Host, HostsCollection
from algoliasearch.http.user_agent import UserAgent


class SearchConfig(BaseConfig):
    def __init__(self, app_id: str, api_key: str) -> None:
        super().__init__(app_id, api_key)

        user_agent = UserAgent().add("Search")

        self.headers = {
            "x-algolia-application-id": app_id,
            "x-algolia-api-key": api_key,
            "user-agent": user_agent.get(),
            "content-type": "application/json",
        }

        http_proxy = environ.get("HTTP_PROXY")
        https_proxy = environ.get("HTTPS_PROXY")

        self.proxies = {}

        if http_proxy is not None:
            self.proxies["http"] = http_proxy
        if https_proxy is not None:
            self.proxies["https"] = https_proxy

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
