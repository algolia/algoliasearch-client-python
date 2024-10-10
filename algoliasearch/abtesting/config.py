from os import environ
from typing import Optional

from algoliasearch.http.base_config import BaseConfig
from algoliasearch.http.hosts import Host, HostsCollection
from algoliasearch.http.user_agent import UserAgent


class AbtestingConfig(BaseConfig):
    def __init__(
        self,
        app_id: Optional[str],
        api_key: Optional[str],
        region: Optional[str] = None,
    ) -> None:
        super().__init__(app_id, api_key)

        user_agent = UserAgent().add("Abtesting")

        if app_id is None or not app_id:
            raise ValueError("`app_id` is missing.")

        if api_key is None or not api_key:
            raise ValueError("`api_key` is missing.")

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
                    else "analytics.{region}.algolia.com".replace(
                        "{region}", region or ""
                    )
                )
            ]
        )
