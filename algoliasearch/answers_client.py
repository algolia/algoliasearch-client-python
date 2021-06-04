from typing import Optional, Union, Dict, Any

from algoliasearch.configs import AnswersConfig
from algoliasearch.helpers import is_async_available
from algoliasearch.http.request_options import RequestOptions
from algoliasearch.http.requester import Requester
from algoliasearch.http.transporter import Transporter
from algoliasearch.http.verb import Verb


class AnswersClient(object):
    def __init__(self, transporter, config):
        # type: (Transporter, AnswersConfig) -> None

        self._transporter = transporter
        self._config = config

    @staticmethod
    def create(app_id=None, api_key=None):
        # type: (Optional[str], Optional[str]) -> AnswersClient  # noqa: E501

        config = AnswersConfig(app_id, api_key)

        return AnswersClient.create_with_config(config)

    @staticmethod
    def create_with_config(config):
        # type: (AnswersConfig) -> AnswersClient

        requester = Requester()
        transporter = Transporter(requester, config)

        client = AnswersClient(transporter, config)

        if is_async_available():
            from algoliasearch.answers_client_async import (
                AnswersClientAsync,
            )
            from algoliasearch.http.transporter_async import TransporterAsync
            from algoliasearch.http.requester_async import RequesterAsync

            return AnswersClientAsync(
                client, TransporterAsync(RequesterAsync(), config), config
            )

        return client

    def predict(
        self, index_name, answers_parameters, request_options=None
    ):  # noqa: E501
        # type: (str, dict, Optional[Union[dict, RequestOptions]]) -> dict

        return self._transporter.write(
            Verb.POST,
            "1/answers/{}/prediction".format(index_name),
            answers_parameters,
            request_options,
        )

    def close(self):
        # type: () -> None

        return self._transporter.close()  # type: ignore
