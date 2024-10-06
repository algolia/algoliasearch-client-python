from os import environ
from typing import Optional

from algoliasearch.http.base_config import BaseConfig
from algoliasearch.http.hosts import Host, HostsCollection
from algoliasearch.http.user_agent import UserAgent


class MonitoringConfig(BaseConfig):
    def __init__(self, app_id: Optional[str], api_key: Optional[str]) -> None:
        super().__init__(app_id, api_key)

        user_agent = UserAgent().add("Monitoring")

        assert app_id, "`app_id` is missing."
        assert api_key, "`api_key` is missing."

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
                Host("status.algolia.com"),
            ]
        )
