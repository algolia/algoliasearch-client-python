import types
from typing import Optional, Type

from algoliasearch.configs import SearchConfig
from algoliasearch.helpers_async import _create_async_methods_in
from algoliasearch.http.transporter_async import TransporterAsync
from algoliasearch.recommend_client import RecommendClient


class RecommendClientAsync(RecommendClient):
    def __init__(self, recommend_client, transporter, search_config):
        # type: (RecommendClient, TransporterAsync, SearchConfig) -> None

        self._recommend_client = recommend_client
        self._transporter_async = transporter

        super(RecommendClientAsync, self).__init__(
            recommend_client._transporter, search_config
        )

        recommend_client = RecommendClient(transporter, search_config)
        recommend_client.__setattr__("_sync", self._sync)
        _create_async_methods_in(self, recommend_client)

    async def __aenter__(self):
        # type: () -> RecommendClientAsync # type: ignore

        return self  # type: ignore

    async def __aexit__(self, exc_type, exc, tb):  # type: ignore
        # type: (Optional[Type[BaseException]], Optional[BaseException],Optional[types.TracebackType]) -> None # noqa: E501

        await self.close_async()  # type: ignore

    async def close_async(self):  # type: ignore
        # type: () -> None

        super().close()

        await self._transporter_async.close()  # type: ignore

    def _sync(self):
        # type: () -> RecommendClient

        return self._recommend_client
