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
