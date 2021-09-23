from typing import Optional, Union, List

from algoliasearch.helpers import is_async_available
from algoliasearch.http.request_options import RequestOptions
from algoliasearch.http.verb import Verb
from algoliasearch.configs import SearchConfig
from algoliasearch.http.requester import Requester
from algoliasearch.http.transporter import Transporter


class RecommendClient(object):
    @property
    def app_id(self):
        # type: () -> str

        return self._config.app_id

    def __init__(self, transporter, search_config):
        # type: (Transporter, SearchConfig) -> None

        self._transporter = transporter
        self._config = search_config

    @staticmethod
    def create(app_id=None, api_key=None):
        # type: (Optional[str], Optional[str]) -> RecommendClient

        config = SearchConfig(app_id, api_key)

        return RecommendClient.create_with_config(config)

    @staticmethod
    def create_with_config(config):
        # type: (SearchConfig) -> RecommendClient

        requester = Requester()
        transporter = Transporter(requester, config)

        client = RecommendClient(transporter, config)

        if is_async_available():
            from algoliasearch.recommend_client_async import RecommendClientAsync
            from algoliasearch.http.transporter_async import TransporterAsync
            from algoliasearch.http.requester_async import RequesterAsync

            return RecommendClientAsync(
                client, TransporterAsync(RequesterAsync(), config), config
            )

        return client

    def get_recommendations(self, queries, request_options=None):
        # type: (List[dict], Optional[Union[dict, RequestOptions]]) -> dict

        for q in queries:
            if "threshold" not in q or q["threshold"] is None:
                q["threshold"] = 0

        return self._transporter.read(
            Verb.POST,
            "1/indexes/*/recommendations",
            {"requests": queries},
            request_options,
        )

    def get_related_products(self, queries, request_options=None):
        # type: (List[dict], Optional[Union[dict, RequestOptions]]) -> dict

        for q in queries:
            q["model"] = "related-products"

        return self.get_recommendations(queries, request_options)

    def get_frequently_bought_together(self, queries, request_options=None):
        # type: (List[dict], Optional[Union[dict, RequestOptions]]) -> dict

        for q in queries:
            q.pop("fallbackParameters", None)
            q["model"] = "bought-together"

        return self.get_recommendations(queries, request_options)

    def close(self):
        # type: () -> None

        return self._transporter.close()  # type: ignore

    def _sync(self):
        # type: () -> RecommendClient

        return self
