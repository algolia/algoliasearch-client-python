import types

import asyncio
from typing import Optional, Type

from algoliasearch.analytics_client import AnalyticsClient
from algoliasearch.configs import AnalyticsConfig
from algoliasearch.helpers_async import _create_async_methods_in
from algoliasearch.http.transporter_async import TransporterAsync


class AnalyticsClientAsync(AnalyticsClient):
    def __init__(self, analytics_client, transporter, search_config):
        # type: (AnalyticsClient, TransporterAsync, AnalyticsConfig) -> None

        self._transporter_async = transporter

        super(AnalyticsClientAsync, self).__init__(
            analytics_client._transporter, search_config
        )

        client = AnalyticsClient(transporter, search_config)

        _create_async_methods_in(self, client)

    @asyncio.coroutine
    def __aenter__(self):
        # type: () -> AnalyticsClientAsync # type: ignore

        return self  # type: ignore

    @asyncio.coroutine
    def __aexit__(self, exc_type, exc, tb):  # type: ignore
        # type: (Optional[Type[BaseException]], Optional[BaseException],Optional[types.TracebackType]) -> None # noqa: E501

        yield from self.close_async()  # type: ignore

    @asyncio.coroutine
    def close_async(self):  # type: ignore
        # type: () -> None

        super().close()

        yield from self._transporter_async.close()  # type: ignore
