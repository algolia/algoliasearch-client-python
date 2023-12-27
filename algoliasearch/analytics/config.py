from os import environ
from typing import Optional

from algoliasearch.http.base_config import BaseConfig
from algoliasearch.http.hosts import Host, HostsCollection
from algoliasearch.http.user_agent import UserAgent


class AnalyticsConfig(BaseConfig):
    def __init__(
        self,
        app_id: Optional[str] = None,
        api_key: Optional[str] = None,
        region: Optional[str] = None,
    ) -> None:
        app_id = environ.get("ALGOLIA_APP_ID") if app_id is None else app_id

        assert app_id, "`app_id` is missing."

        api_key = environ.get("ALGOLIA_API_KEY") if api_key is None else api_key

        assert api_key, "`api_key` is missing."

        self.app_id = str(app_id)
        self.api_key = str(api_key)

        # In milliseconds
        self.read_timeout = 5000
        self.write_timeout = 30000
        self.connect_timeout = 2000

        UserAgent.add("Analytics")

        self.headers = {
            "x-algolia-application-id": app_id,
            "x-algolia-api-key": api_key,
            "user-agent": UserAgent.get(),
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
