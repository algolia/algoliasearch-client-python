from os import environ
from typing import Dict, Literal, Optional
from warnings import warn

from algoliasearch import __version__
from algoliasearch.http.base_config import BaseConfig
from algoliasearch.http.hosts import CallType, Host, HostsCollection
from algoliasearch.http.user_agent import UserAgent


class TransformationOptions:
    """Options for the transformation pipeline."""

    def __init__(
        self,
        region: str,
        *,
        connect_timeout: Optional[int] = None,
        read_timeout: Optional[int] = None,
        write_timeout: Optional[int] = None,
        hosts: Optional[HostsCollection] = None,
        proxies: Optional[Dict[str, str]] = None,
        headers: Optional[Dict[str, str]] = None,
        compression_type: Optional[Literal["gzip"]] = None,
        compression_threshold: Optional[int] = None,
        wait_task_time_before_retry: Optional[int] = None,
    ):
        if not region:
            raise ValueError(
                "`region` is required in `transformation_options`. See https://www.algolia.com/doc/libraries/sdk/methods/ingestion/"
            )
        self.region = region
        self.connect_timeout = connect_timeout
        self.read_timeout = read_timeout
        self.write_timeout = write_timeout
        self.hosts = hosts
        self.proxies = proxies
        self.headers = headers
        self.compression_type: Optional[Literal["gzip"]] = compression_type
        self.compression_threshold = compression_threshold
        self.wait_task_time_before_retry = wait_task_time_before_retry


class SearchConfig(BaseConfig):
    def __init__(
        self,
        app_id: Optional[str],
        api_key: Optional[str],
        transformation_options: Optional["TransformationOptions"] = None,
    ) -> None:
        super().__init__(app_id, api_key)

        # In milliseconds
        self.read_timeout = 5000
        self.write_timeout = 30000
        self.connect_timeout = 2000

        self._user_agent = UserAgent()
        self.add_user_agent("Search", __version__)

        if app_id is None or not app_id:
            raise ValueError("`app_id` is missing.")

        if api_key is None or not api_key:
            raise ValueError("`api_key` is missing.")

        self.headers = {
            "x-algolia-application-id": app_id,
            "x-algolia-api-key": api_key,
            "user-agent": self._user_agent.get(),
            "content-type": "application/json",
        }

        http_proxy = environ.get("HTTP_PROXY")
        https_proxy = environ.get("HTTPS_PROXY")

        self.proxies = {}

        if http_proxy is not None:
            self.proxies["http"] = http_proxy
        if https_proxy is not None:
            self.proxies["https"] = https_proxy

        self.region = None
        self.transformation_options = transformation_options

    def set_transformation_region(self, region: str = ""):
        """@deprecated Set `transformation_options` in the client config before creating the client. See https://www.algolia.com/doc/libraries/sdk/methods/ingestion/"""
        warn(
            "set_transformation_region is deprecated. Set `transformation_options` in the client config before creating the client. Changes after client construction do not affect the existing ingestion transporter. See https://www.algolia.com/doc/libraries/sdk/methods/ingestion/",
            DeprecationWarning,
            stacklevel=2,
        )
        self.region = region
        self.transformation_options = (
            None if not region else TransformationOptions(region=region)
        )

    def set_default_hosts(self):
        if self.hosts is not None:
            return

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
