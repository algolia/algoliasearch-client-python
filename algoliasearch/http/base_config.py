from os import environ
from typing import Dict, Optional

from algoliasearch.http.hosts import HostsCollection


class BaseConfig:
    app_id: Optional[str]
    api_key: Optional[str]

    read_timeout: int
    write_timeout: int
    connect_timeout: int

    wait_task_time_before_retry: Optional[int]

    headers: Dict[str, str]
    proxies: Dict[str, str]

    hosts: HostsCollection

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

        self.wait_task_time_before_retry = None
        self.headers = None
        self.proxies = None
        self.hosts = None
