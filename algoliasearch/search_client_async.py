from algoliasearch.configs import SearchConfig
from algoliasearch.helpers_async import _create_async_methods_in
from algoliasearch.http.requester_async import RequesterAsync
from algoliasearch.http.transporter_async import TransporterAsync
from algoliasearch.search_client import SearchClient
from algoliasearch.search_index_async import SearchIndexAsync


class SearchClientAsync(SearchClient):

    def __init__(self, search_client, transporter, search_config):
        # type: (SearchClient, Transporter, SearchConfig) -> None

        self._search_client = search_client
        self._transporter_async = transporter

        super(SearchClientAsync, self).__init__(transporter, search_config)
        _create_async_methods_in(self)

        self._transporter = search_client._transporter

    def init_index(self, name):
        # type: (str) -> SearchIndexAsync

        index = self._search_client.init_index(name)

        return SearchIndexAsync(
            index, self._transporter_async, self._config, name)
