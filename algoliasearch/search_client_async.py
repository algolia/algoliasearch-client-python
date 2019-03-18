import types

import asyncio
from typing import Optional, Type

from algoliasearch.configs import SearchConfig
from algoliasearch.helpers_async import _create_async_methods_in
from algoliasearch.http.transporter_async import TransporterAsync
from algoliasearch.search_client import SearchClient
from algoliasearch.search_index_async import SearchIndexAsync


class SearchClientAsync(SearchClient):

    def __init__(self, search_client, transporter, search_config):
        # type: (SearchClient, TransporterAsync, SearchConfig) -> None

        self._search_client = search_client
        self._transporter_async = transporter

        super(SearchClientAsync, self).__init__(
            search_client._transporter,
            search_config
        )

        search_client = SearchClient(transporter, search_config)
        search_client.__setattr__('init_index', self.init_index)
        search_client.__setattr__('_sync', self._sync)
        _create_async_methods_in(self, search_client)

    def init_index(self, name):
        # type: (str) -> SearchIndexAsync

        index = self._search_client.init_index(name)

        return SearchIndexAsync(
            index, self._transporter_async, self._config, name)

    def close(self):
        # type: () -> types.GeneratorType

        return self._transporter_async._requester.close()  # type: ignore

    @asyncio.coroutine  # type: ignore
    def __aenter__(self):
        # type: () -> SearchClientAsync

        return self  # type: ignore

    @asyncio.coroutine  # type: ignore
    def __aexit__(self, exc_type, exc, tb):
        # type: (Optional[Type[BaseException]], Optional[BaseException],Optional[types.TracebackType]) -> None # noqa: E501

        yield from self.close()

    def _sync(self):
        # type: () -> SearchClient

        return self._search_client
