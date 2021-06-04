import types
import asyncio
from typing import Optional, Type

from algoliasearch.answers_client import AnswersClient
from algoliasearch.configs import AnswersConfig
from algoliasearch.helpers_async import _create_async_methods_in
from algoliasearch.http.transporter_async import TransporterAsync


class AnswersClientAsync(AnswersClient):
    def __init__(self, answers_client, transporter, search_config):
        # type: (AnswersClient, TransporterAsync, AnswersConfig) -> None # noqa: E501

        self._transporter_async = transporter

        super(AnswersClientAsync, self).__init__(answers_client._transporter, search_config)

        client = AnswersClient(transporter, search_config)

        _create_async_methods_in(self, client)

    @asyncio.coroutine
    def __aenter__(self):
        # type: () -> AnswersClientAsync # type: ignore

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
