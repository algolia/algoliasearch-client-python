import base64
import hashlib
import hmac
import re
import time
from typing import Iterator, List, Optional, Union

from algoliasearch.configs import SearchConfig
from algoliasearch.exceptions import ValidUntilNotFoundException
from algoliasearch.helpers import build_raw_response_batch, endpoint, is_async_available
from algoliasearch.http.hosts import CallType
from algoliasearch.http.request_options import RequestOptions
from algoliasearch.http.requester import Requester
from algoliasearch.http.serializer import QueryParametersSerializer
from algoliasearch.http.transporter import Transporter
from algoliasearch.http.verb import Verb
from algoliasearch.responses import (
    AddApiKeyResponse,
    DeleteApiKeyResponse,
    DictionaryResponse,
    IndexingResponse,
    MultipleIndexBatchIndexingResponse,
    RestoreApiKeyResponse,
    UpdateApiKeyResponse,
)
from algoliasearch.search_index import SearchIndex


class SearchClient(object):
    @property
    def app_id(self):
        # type: () -> str

        return self._config.app_id

    def __init__(self, transporter, search_config):
        # type: (Transporter, SearchConfig) -> None

        self._transporter = transporter
        self._config = search_config

    def init_index(self, name):
        # type: (str) -> SearchIndex

        return SearchIndex(self._transporter, self._config, name)

    @staticmethod
    def create(app_id=None, api_key=None):
        # type: (Optional[str], Optional[str]) -> SearchClient

        config = SearchConfig(app_id, api_key)

        return SearchClient.create_with_config(config)

    @staticmethod
    def create_with_config(config):
        # type: (SearchConfig) -> SearchClient

        requester = Requester()
        transporter = Transporter(requester, config)

        client = SearchClient(transporter, config)

        if is_async_available():
            from algoliasearch.http.requester_async import RequesterAsync
            from algoliasearch.http.transporter_async import TransporterAsync
            from algoliasearch.search_client_async import SearchClientAsync

            return SearchClientAsync(
                client, TransporterAsync(RequesterAsync(), config), config
            )

        return client

    def move_index(self, src_index_name, dst_index_name, request_options=None):
        # type: (str, str, Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        raw_response = self._transporter.write(
            Verb.POST,
            endpoint("1/indexes/{}/operation", src_index_name),
            {"operation": "move", "destination": dst_index_name},
            request_options,
        )

        return IndexingResponse(self.init_index(src_index_name), [raw_response])

    def copy_index(self, src_index_name, dst_index_name, request_options=None):
        # type: (str, str, Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        raw_response = self._transporter.write(
            Verb.POST,
            endpoint("1/indexes/{}/operation", src_index_name),
            {"operation": "copy", "destination": dst_index_name},
            request_options,
        )

        return IndexingResponse(self.init_index(src_index_name), [raw_response])

    def copy_settings(self, src_index_name, dst_index_name, request_options=None):
        # type: (str, str, Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        if request_options is None:
            request_options = {}

        request_options["scope"] = ["settings"]

        return self.copy_index(src_index_name, dst_index_name, request_options)

    def copy_synonyms(self, src_index_name, dst_index_name, request_options=None):
        # type: (str, str, Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        if request_options is None:
            request_options = {}

        request_options["scope"] = ["synonyms"]

        return self.copy_index(src_index_name, dst_index_name, request_options)

    def copy_rules(self, src_index_name, dst_index_name, request_options=None):
        # type: (str, str, Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        if request_options is None:
            request_options = {}

        request_options["scope"] = ["rules"]

        return self.copy_index(src_index_name, dst_index_name, request_options)

    def assign_user_id(self, user_id, cluster, request_options=None):
        # type: (str, str,Optional[Union[dict, RequestOptions]]) -> dict

        if request_options is None:
            request_options = RequestOptions.create(self._config)

        request_options["X-Algolia-User-ID"] = user_id

        return self._transporter.write(
            Verb.POST, "1/clusters/mapping", {"cluster": cluster}, request_options
        )

    def assign_user_ids(self, user_ids, cluster, request_options=None):
        # type: (Union[List[dict], Iterator[dict]], str, Optional[Union[dict, RequestOptions]]) -> dict # noqa: E501

        return self._transporter.write(
            Verb.POST,
            "1/clusters/mapping/batch",
            {"cluster": cluster, "users": user_ids},
            request_options,
        )

    def remove_user_id(self, user_id, request_options=None):
        # type: (str, Optional[Union[dict, RequestOptions]]) -> dict

        if request_options is None:
            request_options = RequestOptions.create(self._config)

        request_options["X-Algolia-User-ID"] = user_id

        return self._transporter.write(
            Verb.DELETE, "1/clusters/mapping", None, request_options
        )

    def list_clusters(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> dict

        return self._transporter.read(Verb.GET, "1/clusters", {}, request_options)

    def get_user_id(self, user_id, request_options=None):
        # type: (str, Optional[Union[dict, RequestOptions]]) -> dict

        return self._transporter.read(
            Verb.GET, endpoint("1/clusters/mapping/{}", user_id), None, request_options
        )

    def list_user_ids(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> dict

        return self._transporter.read(
            Verb.GET, "1/clusters/mapping", None, request_options
        )

    def get_top_user_ids(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> dict

        return self._transporter.read(
            Verb.GET, "1/clusters/mapping/top", None, request_options
        )

    def search_user_ids(self, query, request_options=None):
        # type: (str, Optional[Union[dict, RequestOptions]]) -> dict

        return self._transporter.read(
            Verb.POST, "1/clusters/mapping/search", {"query": query}, request_options
        )

    def has_pending_mappings(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> dict

        retrieve_mappings = None
        if isinstance(request_options, dict):
            retrieve_mappings = request_options.pop(
                "retrieveMappings", retrieve_mappings
            )

        if retrieve_mappings:
            if request_options is None or isinstance(request_options, dict):
                request_options = RequestOptions.create(self._config, request_options)

            request_options.query_parameters["getClusters"] = retrieve_mappings

        return self._transporter.read(
            Verb.GET, "1/clusters/mapping/pending", None, request_options
        )

    def list_api_keys(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> dict

        return self._transporter.read(Verb.GET, "1/keys", None, request_options)

    def get_api_key(self, key, request_options=None):
        # type: (str, Optional[Union[dict, RequestOptions]]) -> dict

        return self._transporter.read(
            Verb.GET, endpoint("1/keys/{}", key), None, request_options
        )

    def delete_api_key(self, key, request_options=None):
        # type: (str, Optional[Union[dict, RequestOptions]]) -> DeleteApiKeyResponse # noqa: E501

        raw_response = self._transporter.write(
            Verb.DELETE, endpoint("1/keys/{}", key), None, request_options
        )
        return DeleteApiKeyResponse(self, raw_response, key)

    def add_api_key(self, acl, request_options=None):
        # type: (list, Optional[Union[dict, RequestOptions]]) -> AddApiKeyResponse # noqa: E501

        raw_response = self._transporter.write(
            Verb.POST, "1/keys", {"acl": acl}, request_options
        )

        return AddApiKeyResponse(self, raw_response)

    def update_api_key(self, key, request_options=None):
        # type: (str, Optional[Union[dict, RequestOptions]]) -> UpdateApiKeyResponse # noqa: E501

        if not isinstance(request_options, RequestOptions):
            request_options = RequestOptions.create(self._config, request_options)

        raw_response = self._transporter.write(
            Verb.PUT, endpoint("1/keys/{}", key), {}, request_options
        )

        return UpdateApiKeyResponse(self, raw_response, request_options)

    def restore_api_key(self, key, request_options=None):
        # type: (str, Optional[Union[dict, RequestOptions]]) -> RestoreApiKeyResponse # noqa: E501

        raw_response = self._transporter.write(
            Verb.POST, endpoint("1/keys/{}/restore", key), None, request_options
        )

        return RestoreApiKeyResponse(self, raw_response, key)

    @staticmethod
    def generate_secured_api_key(parent_api_key, restrictions):
        # type: (str, dict) -> str

        query_parameters = QueryParametersSerializer.serialize(restrictions)

        secured_key = hmac.new(
            parent_api_key.encode("utf-8"),
            query_parameters.encode("utf-8"),
            hashlib.sha256,
        ).hexdigest()

        base64encoded = base64.b64encode(
            ("{}{}".format(secured_key, query_parameters)).encode("utf-8")
        )

        return str(base64encoded.decode("utf-8"))

    @staticmethod
    def get_secured_api_key_remaining_validity(api_key):
        # type: (str) -> int

        decoded_string = base64.b64decode(api_key)

        match = re.search(r"validUntil=(\d+)", str(decoded_string))

        if match is None:
            raise ValidUntilNotFoundException("ValidUntil not found in api key.")

        return int(match.group(1)) - int(round(time.time()))

    def list_indices(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> dict

        return self._transporter.read(Verb.GET, "1/indexes", None, request_options)

    def get_logs(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> dict

        return self._transporter.read(Verb.GET, "1/logs", None, request_options)

    def multiple_queries(self, queries, request_options=None):
        # type: (List[dict], Optional[Union[dict, RequestOptions]]) -> dict

        return self._transporter.read(
            Verb.POST, "1/indexes/*/queries", {"requests": queries}, request_options
        )

    def multiple_get_objects(self, requests, request_options=None):
        # type: (List[dict], Optional[Union[dict, RequestOptions]]) -> dict

        return self._transporter.read(
            Verb.POST, "1/indexes/*/objects", {"requests": requests}, request_options
        )

    def multiple_batch(self, operations, request_options=None):
        # type: (List[dict], Optional[Union[dict, RequestOptions]]) -> MultipleIndexBatchIndexingResponse # noqa: E501

        raw_response = self._transporter.write(
            Verb.POST, "1/indexes/*/batch", {"requests": operations}, request_options
        )

        return MultipleIndexBatchIndexingResponse(self, raw_response)

    def wait_task(self, index_name, task_id, request_options=None):
        # type: (str, int, Optional[Union[dict, RequestOptions]]) -> None

        self.init_index(index_name).wait_task(task_id, request_options)

    def save_dictionary_entries(
        self, dictionary, dictionary_entries, request_options=None
    ):
        # type: (str, List[dict], Optional[Union[dict, RequestOptions]]) -> DictionaryResponse # noqa: E501

        raw_response = self._transporter.write(
            Verb.POST,
            endpoint("1/dictionaries/{}/batch", dictionary),
            {
                "clearExistingDictionaryEntries": False,
                "requests": build_raw_response_batch("addEntry", dictionary_entries),
            },
            request_options,
        )

        return DictionaryResponse(self, raw_response)

    def replace_dictionary_entries(
        self, dictionary, dictionary_entries, request_options=None
    ):
        # type: (str, List[dict], Optional[Union[dict, RequestOptions]]) -> DictionaryResponse # noqa: E501

        raw_response = self._transporter.write(
            Verb.POST,
            endpoint("1/dictionaries/{}/batch", dictionary),
            {
                "clearExistingDictionaryEntries": True,
                "requests": build_raw_response_batch("addEntry", dictionary_entries),
            },
            request_options,
        )

        return DictionaryResponse(self, raw_response)

    def delete_dictionary_entries(self, dictionary, object_ids, request_options=None):
        # type: (str, Iterator[str], Optional[Union[dict, RequestOptions]])-> DictionaryResponse # noqa: E501

        request = [{"objectID": object_id} for object_id in object_ids]

        raw_response = self._transporter.write(
            Verb.POST,
            endpoint("1/dictionaries/{}/batch", dictionary),
            {
                "clearExistingDictionaryEntries": False,
                "requests": build_raw_response_batch("deleteEntry", request),
            },
            request_options,
        )

        return DictionaryResponse(self, raw_response)

    def clear_dictionary_entries(self, dictionary, request_options=None):
        # type: (str, Optional[Union[dict, RequestOptions]]) -> DictionaryResponse # noqa: E501

        return self.replace_dictionary_entries(dictionary, [], request_options)

    def search_dictionary_entries(self, dictionary, query, request_options=None):
        # type: (str, str, Optional[Union[dict, RequestOptions]]) -> dict

        return self._transporter.read(
            Verb.POST,
            endpoint("1/dictionaries/{}/search", dictionary),
            {"query": query},
            request_options,
        )

    def set_dictionary_settings(self, dictionary_settings, request_options=None):
        # type: (dict, Optional[Union[dict, RequestOptions]])-> DictionaryResponse # noqa: E501

        raw_response = self._transporter.write(
            Verb.PUT, "1/dictionaries/*/settings", dictionary_settings, request_options
        )

        return DictionaryResponse(self, raw_response)

    def get_dictionary_settings(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> dict

        return self._transporter.read(
            Verb.GET, "1/dictionaries/*/settings", {}, request_options
        )

    def close(self):
        # type: () -> None

        return self._transporter.close()  # type: ignore

    def _sync(self):
        # type: () -> SearchClient

        return self

    def custom_request(self, data, uri, method, call_type, request_options=None):
        # type: (dict, str, str, int, Optional[Union[dict, RequestOptions]]) -> dict

        if call_type == CallType.WRITE:
            return self._transporter.write(method, uri, data, request_options)
        else:
            return self._transporter.read(method, uri, data, request_options)
