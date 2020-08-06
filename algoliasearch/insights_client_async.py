import types

import asyncio
from typing import Optional, Type

from algoliasearch.configs import InsightsConfig
from algoliasearch.helpers_async import _create_async_methods_in
from algoliasearch.http.transporter_async import TransporterAsync
from algoliasearch.insights_client import InsightsClient, UserInsightsClient


class InsightsClientAsync(InsightsClient):
    def __init__(self, insights_client, transporter, insights_config):
        # type: (InsightsClient, TransporterAsync, InsightsConfig) -> None

        self._transporter_async = transporter

        super(InsightsClientAsync, self).__init__(
            insights_client._transporter, insights_config
        )

        client = InsightsClient(transporter, insights_config)
        _create_async_methods_in(self, client)

    def user(self, user_token):
        # type: (str) -> UserInsightsClientAsync

        return UserInsightsClientAsync(self, user_token)

    @asyncio.coroutine
    def __aenter__(self):
        # type: () -> InsightsClientAsync # type: ignore

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


class UserInsightsClientAsync(UserInsightsClient):
    def __init__(self, insights_client, user_token):
        # type: (InsightsClient, str) -> None

        super(UserInsightsClientAsync, self).__init__(insights_client, user_token)

        client = UserInsightsClient(insights_client, user_token)

        _create_async_methods_in(self, client)
