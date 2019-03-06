from algoliasearch.analytics_client import AnalyticsClient
from algoliasearch.configs import AnalyticsConfig
from algoliasearch.helpers_async import _create_async_methods_in
from algoliasearch.http.transporter import Transporter


class AnalyticsClientAsync(AnalyticsClient):
    def __init__(self, analytics_client, transporter, search_config):
        # type: (AnalyticsClient, Transporter, AnalyticsConfig) -> None

        super(AnalyticsClientAsync, self).__init__(
            analytics_client._transporter,
            search_config
        )

        client = AnalyticsClient(transporter, search_config)

        _create_async_methods_in(self, client)
