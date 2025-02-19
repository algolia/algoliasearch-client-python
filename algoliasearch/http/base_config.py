from os import environ
from typing import Dict, Optional

from algoliasearch.http.hosts import HostsCollection
from algoliasearch.http.user_agent import UserAgent


class BaseConfig:
    def __init__(self, app_id: Optional[str] = None, api_key: Optional[str] = None):
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

        self.wait_task_time_before_retry: Optional[int] = None
        self.headers: Dict[str, str] = {}
        self.proxies: Optional[Dict[str, str]] = None
        self.hosts: Optional[HostsCollection] = None

        self._user_agent: UserAgent = UserAgent()

    def set_client_api_key(self, api_key: str) -> None:
        """Sets a new API key to authenticate requests."""
        self.api_key = api_key
        self.headers["x-algolia-api-key"] = api_key

    def add_user_agent(self, segment: str, version: Optional[str] = None) -> None:
        """adds a segment to the default user agent, and update the headers sent with each requests as well"""
        self._user_agent = self._user_agent.add(segment, version)
        self.headers["user-agent"] = self._user_agent.get()
