from typing import Any, Dict, List

from algoliasearch.http.base_config import BaseConfig
from algoliasearch.http.hosts import Host
from algoliasearch.http.request_options import RequestOptions
from algoliasearch.http.retry import RetryStrategy


class BaseTransporter:
    _config: BaseConfig
    _retry_strategy: RetryStrategy
    _hosts: List[Host]

    def __init__(self, config: BaseConfig) -> None:
        self._config = config
        self._retry_strategy = RetryStrategy()
        self._hosts = []

    def prepare(
        self,
        request_options: RequestOptions,
        use_read_transporter: bool,
    ) -> Dict[str, Any]:
        query_parameters = dict(request_options.query_parameters)

        if use_read_transporter:
            self._timeout = request_options.timeouts["read"]
            self._hosts = self._config.hosts.read()
            if isinstance(request_options.data, dict):
                query_parameters.update(request_options.data)
            return query_parameters

        self._timeout = request_options.timeouts["write"]
        self._hosts = self._config.hosts.write()

    def build_path(self, path, query_parameters):
        if query_parameters is not None and len(query_parameters) > 0:
            return "{}?{}".format(
                path,
                "&".join(
                    [
                        "{}={}".format(key, value)
                        for key, value in query_parameters.items()
                    ]
                ),
            )
        return path

    def build_url(self, host, path):
        return "{}://{}{}".format(
            host.scheme,
            host.url + (":{}".format(host.port) if host.port else ""),
            path,
        )

    def get_proxy(self, url):
        if url.startswith("https"):
            return self._config.proxies.get("https")
        elif url.startswith("http"):
            return self._config.proxies.get("http")
        else:
            return None
