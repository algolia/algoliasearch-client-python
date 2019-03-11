import asyncio

from algoliasearch.configs import SearchConfig
from algoliasearch.helpers_async import _create_async_methods_in
from algoliasearch.http.transporter import Transporter
from algoliasearch.search_client import SearchClient
from algoliasearch.search_index_async import SearchIndexAsync


class SearchClientAsync(SearchClient):

    def __init__(self, search_client, transporter, search_config):
        # type: (SearchClient, Transporter, SearchConfig) -> None

        self._search_client = search_client
        self._transporter_async = transporter

        super(SearchClientAsync, self).__init__(
            search_client._transporter,
            search_config
        )

        search_client = SearchClient(transporter, search_config)
        search_client.__setattr__('init_index', self.init_index)
        search_client.__setattr__('sync', self.sync)
        _create_async_methods_in(self, search_client)

    def init_index(self, name):
        # type: (str) -> SearchIndexAsync

        index = self._search_client.init_index(name)

        return SearchIndexAsync(
            index, self._transporter_async, self._config, name)

    def sync(self):
        # type: () -> SearchClient

        return self._search_client
