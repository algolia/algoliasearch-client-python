from typing import Optional, Union

from algoliasearch.configs import PersonalizationConfig
from algoliasearch.helpers import is_async_available
from algoliasearch.http.request_options import RequestOptions
from algoliasearch.http.requester import Requester
from algoliasearch.http.transporter import Transporter
from algoliasearch.http.verb import Verb


class PersonalizationClient(object):
    def __init__(self, transporter, config):
        # type: (Transporter, PersonalizationConfig) -> None

        self._transporter = transporter
        self._config = config

    @staticmethod
    def create(app_id=None, api_key=None, region=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> PersonalizationClient  # noqa: E501

        config = PersonalizationConfig(app_id, api_key, region)

        return PersonalizationClient.create_with_config(config)

    @staticmethod
    def create_with_config(config):
        # type: (PersonalizationConfig) -> PersonalizationClient

        requester = Requester()
        transporter = Transporter(requester, config)

        client = PersonalizationClient(transporter, config)

        if is_async_available():
            from algoliasearch.personalization_client_async import (
                PersonalizationClientAsync,
            )
            from algoliasearch.http.transporter_async import TransporterAsync
            from algoliasearch.http.requester_async import RequesterAsync

            return PersonalizationClientAsync(
                client, TransporterAsync(RequesterAsync(), config), config
            )

        return client

    def set_personalization_strategy(
        self, personalization_strategy, request_options=None
    ):  # noqa: E501
        # type: (dict, Optional[Union[dict, RequestOptions]]) -> dict

        return self._transporter.write(
            Verb.POST,
            "1/strategies/personalization",
            personalization_strategy,
            request_options,
        )

    def get_personalization_strategy(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> dict

        return self._transporter.read(
            Verb.GET, "1/strategies/personalization", None, request_options
        )

    def close(self):
        # type: () -> None

        return self._transporter.close()  # type: ignore
