import types

from algoliasearch.analytics_client import AnalyticsClient
from algoliasearch.configs import AnalyticsConfig
from algoliasearch.helpers_async import _create_async_methods_in
from algoliasearch.http.transporter_async import TransporterAsync


class AnalyticsClientAsync(AnalyticsClient):
    def __init__(self, analytics_client, transporter, search_config):
        # type: (AnalyticsClient, TransporterAsync, AnalyticsConfig) -> None

        self._transporter_async = transporter

        super(AnalyticsClientAsync, self).__init__(
            analytics_client._transporter,
            search_config
        )

        client = AnalyticsClient(transporter, search_config)

        _create_async_methods_in(self, client)

    def close(self):
        # type: () -> types.GeneratorType

        return self._transporter_async._requester.close()  # type: ignore
