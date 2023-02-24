import types
from typing import Optional, Type

from algoliasearch.configs import PersonalizationConfig
from algoliasearch.helpers_async import _create_async_methods_in
from algoliasearch.http.transporter_async import TransporterAsync
from algoliasearch.personalization_client import PersonalizationClient


class PersonalizationClientAsync(PersonalizationClient):
    def __init__(self, personalization_client, transporter, search_config):
        # type: (PersonalizationClient, TransporterAsync, PersonalizationConfig) -> None # noqa: E501

        self._transporter_async = transporter

        super(PersonalizationClientAsync, self).__init__(
            personalization_client._transporter, search_config
        )

        client = PersonalizationClient(transporter, search_config)

        _create_async_methods_in(self, client)

    async def __aenter__(self):
        # type: () -> PersonalizationClientAsync # type: ignore

        return self  # type: ignore

    async def __aexit__(self, exc_type, exc, tb):  # type: ignore
        # type: (Optional[Type[BaseException]], Optional[BaseException],Optional[types.TracebackType]) -> None # noqa: E501

        await self.close_async()  # type: ignore

    async def close_async(self):  # type: ignore
        # type: () -> None

        super().close()

        await self._transporter_async.close()  # type: ignore
