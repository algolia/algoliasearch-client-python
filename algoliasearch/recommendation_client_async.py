import types
import asyncio
from typing import Optional, Type

from algoliasearch.recommendation_client import RecommendationClient
from algoliasearch.configs import RecommendationConfig
from algoliasearch.helpers_async import _create_async_methods_in
from algoliasearch.http.transporter_async import TransporterAsync


class RecommendationClientAsync(RecommendationClient):
    def __init__(self, recommendation_client, transporter, search_config):
        # type: (RecommendationClient, TransporterAsync, RecommendationConfig) -> None # noqa: E501

        self._transporter_async = transporter

        super(RecommendationClientAsync, self).__init__(
            recommendation_client._transporter, search_config
        )

        client = RecommendationClient(transporter, search_config)

        _create_async_methods_in(self, client)

    async def __aenter__(self):
        # type: () -> RecommendationClientAsync # type: ignore

        return self  # type: ignore

    async def __aexit__(self, exc_type, exc, tb):  # type: ignore
        # type: (Optional[Type[BaseException]], Optional[BaseException],Optional[types.TracebackType]) -> None # noqa: E501

        await self.close_async()  # type: ignore

    async def close_async(self):  # type: ignore
        # type: () -> None

        super().close()

        await self._transporter_async.close()  # type: ignore
