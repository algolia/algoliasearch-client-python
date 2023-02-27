from typing import List, Optional, Union

from algoliasearch.configs import InsightsConfig
from algoliasearch.helpers import is_async_available
from algoliasearch.http.request_options import RequestOptions
from algoliasearch.http.requester import Requester
from algoliasearch.http.transporter import Transporter
from algoliasearch.http.verb import Verb


class InsightsClient(object):
    def __init__(self, transporter, search_config):
        # type: (Transporter, InsightsConfig) -> None

        self._transporter = transporter
        self._config = search_config

    @staticmethod
    def create(app_id=None, api_key=None, region=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> InsightsClient

        config = InsightsConfig(app_id, api_key, region)

        return InsightsClient.create_with_config(config)

    @staticmethod
    def create_with_config(config):
        # type: (InsightsConfig) -> InsightsClient

        requester = Requester()
        transporter = Transporter(requester, config)

        client = InsightsClient(transporter, config)

        if is_async_available():
            from algoliasearch.http.requester_async import RequesterAsync
            from algoliasearch.http.transporter_async import TransporterAsync
            from algoliasearch.insights_client_async import InsightsClientAsync

            return InsightsClientAsync(
                client, TransporterAsync(RequesterAsync(), config), config
            )

        return client

    def user(self, user_token):
        # type: (str) -> UserInsightsClient

        return UserInsightsClient(self, user_token)

    def send_event(self, params, request_options=None):
        # type: (dict, Optional[Union[dict, RequestOptions]]) -> dict

        return self.send_events([params], request_options)

    def send_events(self, events, request_options=None):
        # type: (List[dict], Optional[Union[dict, RequestOptions]]) -> dict

        return self._transporter.write(
            Verb.POST, "1/events", {"events": events}, request_options
        )

    def close(self):
        # type: () -> None

        return self._transporter.close()  # type: ignore


class UserInsightsClient:
    def __init__(self, insights_client, user_token):
        # type: (InsightsClient, str) -> None

        self._insights_client = insights_client
        self._user_token = user_token

    def clicked_object_ids(
        self, event_name, index_name, object_ids, request_options=None
    ):
        # type: (str, str, List[str], Optional[Union[dict, RequestOptions]]) -> dict  # noqa: E501

        return self._insights_client.send_event(
            {
                "eventType": "click",
                "eventName": event_name,
                "index": index_name,
                "userToken": self._user_token,
                "objectIds": object_ids,
            },
            request_options,
        )

    def clicked_object_ids_after_search(
        self,
        event_name,
        index_name,
        object_ids,
        positions,
        query_id,
        request_options=None,
    ):
        # type: (str, str, List[str], List[int], str, Optional[Union[dict, RequestOptions]]) -> dict  # noqa: E501

        return self._insights_client.send_event(
            {
                "eventType": "click",
                "eventName": event_name,
                "index": index_name,
                "userToken": self._user_token,
                "objectIds": object_ids,
                "positions": positions,
                "queryId": query_id,
            },
            request_options,
        )

    def clicked_filters(self, event_name, index_name, filters, request_options=None):
        # type: (str, str, List[str], Optional[Union[dict, RequestOptions]]) -> dict  # noqa: E501

        return self._insights_client.send_event(
            {
                "eventType": "click",
                "eventName": event_name,
                "index": index_name,
                "userToken": self._user_token,
                "filters": filters,
            },
            request_options,
        )

    def converted_object_ids(
        self, event_name, index_name, object_ids, request_options=None
    ):
        # type: (str, str, List[str], Optional[Union[dict, RequestOptions]]) -> dict  # noqa: E501

        return self._insights_client.send_event(
            {
                "eventType": "conversion",
                "eventName": event_name,
                "index": index_name,
                "userToken": self._user_token,
                "objectIds": object_ids,
            },
            request_options,
        )

    def converted_object_ids_after_search(
        self, event_name, index_name, object_ids, query_id, request_options=None
    ):
        # type: (str, str, List[str], str, Optional[Union[dict, RequestOptions]]) -> dict  # noqa: E501

        return self._insights_client.send_event(
            {
                "eventType": "conversion",
                "eventName": event_name,
                "index": index_name,
                "userToken": self._user_token,
                "objectIds": object_ids,
                "queryId": query_id,
            },
            request_options,
        )

    def converted_filters(self, event_name, index_name, filters, request_options=None):
        # type: (str, str, List[str], Optional[Union[dict, RequestOptions]]) -> dict  # noqa: E501

        return self._insights_client.send_event(
            {
                "eventType": "conversion",
                "eventName": event_name,
                "index": index_name,
                "userToken": self._user_token,
                "filters": filters,
            },
            request_options,
        )

    def viewed_object_ids(
        self, event_name, index_name, object_ids, request_options=None
    ):
        # type: (str, str, List[str], Optional[Union[dict, RequestOptions]]) -> dict  # noqa: E501

        return self._insights_client.send_event(
            {
                "eventType": "view",
                "eventName": event_name,
                "index": index_name,
                "userToken": self._user_token,
                "objectIds": object_ids,
            },
            request_options,
        )

    def viewed_filters(self, event_name, index_name, filters, request_options=None):
        # type: (str, str, List[str], Optional[Union[dict, RequestOptions]]) -> dict  # noqa: E501

        return self._insights_client.send_event(
            {
                "eventType": "view",
                "eventName": event_name,
                "index": index_name,
                "userToken": self._user_token,
                "filters": filters,
            },
            request_options,
        )
