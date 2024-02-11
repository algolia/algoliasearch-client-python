from os import environ
from typing import Optional

from algoliasearch.http.base_config import BaseConfig
from algoliasearch.http.hosts import Host, HostsCollection
from algoliasearch.http.user_agent import UserAgent


class IngestionConfig(BaseConfig):
    def __init__(
        self,
        app_id: Optional[str] = None,
        api_key: Optional[str] = None,
        region: str = None,
    ) -> None:
        super().__init__(app_id, api_key)

        user_agent = UserAgent().add("Ingestion")

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

        self.region = region
        _regions = ["eu", "us"]

        if not region or (region is not None and region not in _regions):
            raise ValueError(
                f"`region` is required and must be one of the following: {', '.join(_regions)}"
            )

        self.hosts = HostsCollection(
            [Host("data.{region}.algolia.com".replace("{region}", region))]
        )
