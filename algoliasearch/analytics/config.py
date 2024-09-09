from os import environ
from typing import Optional

from algoliasearch.http.base_config import BaseConfig
from algoliasearch.http.hosts import Host, HostsCollection
from algoliasearch.http.user_agent import UserAgent


class AnalyticsConfig(BaseConfig):
    def __init__(self, app_id: str, api_key: str, region: Optional[str] = None) -> None:
        super().__init__(app_id, api_key)

        user_agent = UserAgent().add("Analytics")

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

        self.region = region
        _regions = ["de", "us"]

        if region is not None and region not in _regions:
            raise ValueError(
                f"`region` must be one of the following: {', '.join(_regions)}"
            )

        self.hosts = HostsCollection(
            [
                Host(
                    "analytics.algolia.com"
                    if region is None
                    else "analytics.{region}.algolia.com".replace("{region}", region)
                )
            ]
        )
