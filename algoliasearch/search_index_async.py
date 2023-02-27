import asyncio
import copy
import math
from typing import Callable, Dict, Iterator, List, Optional, Union

from algoliasearch.configs import SearchConfig
from algoliasearch.exceptions import ObjectNotFoundException, RequestException
from algoliasearch.helpers import endpoint
from algoliasearch.helpers_async import _create_async_methods_in
from algoliasearch.http.request_options import RequestOptions
from algoliasearch.http.serializer import SettingsDeserializer
from algoliasearch.http.transporter_async import TransporterAsync
from algoliasearch.http.verb import Verb
from algoliasearch.iterators_async import (
    ObjectIteratorAsync,
    RuleIteratorAsync,
    SynonymIteratorAsync,
)
from algoliasearch.responses import MultipleResponse
from algoliasearch.search_client import SearchClient
from algoliasearch.search_index import SearchIndex


class SearchIndexAsync(SearchIndex):
    def __init__(self, search_index, transporter, config, name):
        # type: (SearchIndex, TransporterAsync, SearchConfig, str) -> None

        self._search_index = search_index
        self._transporter_async = transporter

        super(SearchIndexAsync, self).__init__(search_index._transporter, config, name)

        search_index = SearchIndex(transporter, config, name)
        search_index.__setattr__("_sync", self._sync)

        _create_async_methods_in(self, search_index)

    async def wait_task_async(self, task_id, request_options=None):  # type: ignore
        # type: (int, Optional[Union[dict, RequestOptions]]) -> None

        retries_count = 1

        while True:
            task = await self.get_task_async(task_id, request_options)  # type: ignore

            if task["status"] == "published":
                break

            retries_count += 1
            factor = math.ceil(retries_count / 10)
            sleep_for = factor * self._config.wait_task_time_before_retry

            await asyncio.sleep(sleep_for / 1000000.0)
            return

    def browse_objects_async(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> ObjectIteratorAsync

        return ObjectIteratorAsync(self._transporter_async, self._name, request_options)

    def browse_synonyms_async(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> SynonymIteratorAsync

        return SynonymIteratorAsync(
            self._transporter_async, self._name, request_options
        )

    def browse_rules_async(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> RuleIteratorAsync

        return RuleIteratorAsync(self._transporter_async, self._name, request_options)

    def exists_async(self, request_options=None):  # type: ignore # noqa: E501
        # type: (Optional[Union[dict, RequestOptions]]) -> bool

        try:
            yield from self.get_settings_async(request_options)
        except RequestException as e:
            if e.status_code == 404:
                return False
            raise e

        return True

    def get_settings_async(self, request_options=None):  # type: ignore
        # type: (Optional[Union[dict, RequestOptions]]) -> dict

        if request_options is None or isinstance(request_options, dict):
            request_options = RequestOptions.create(self._config, request_options)

        request_options.query_parameters["getVersion"] = 2

        raw_response = yield from self._transporter_async.read(
            Verb.GET,
            endpoint("1/indexes/{}/settings", self._name),
            None,
            request_options,
        )

        return SettingsDeserializer.deserialize(raw_response)

    def find_object_async(self, callback, request_options=None):  # type: ignore # noqa: E501
        # type: (Callable[[Dict[str, any]], bool], Optional[Union[dict, RequestOptions]]) -> dict # noqa: E501

        paginate = True
        query = ""
        page = 0

        if isinstance(request_options, dict):
            request_options = copy.copy(request_options)
            paginate = request_options.pop("paginate", paginate)
            query = request_options.pop("query", query)

        request_options = RequestOptions.create(self._config, request_options)

        while True:
            request_options.data["page"] = page

            res = yield from self.search_async(query, request_options)  # type: ignore # noqa: E501

            for pos, hit in enumerate(res["hits"]):
                if callback(hit):
                    return {
                        "object": hit,
                        "position": pos,
                        "page": page,
                    }

            has_next_page = page + 1 < int(res["nbPages"])

            if not paginate or not has_next_page:
                raise ObjectNotFoundException

            page += 1

    def replace_all_objects_async(  # type: ignore
        self,
        objects,
        request_options=None,
    ):
        # type: (Union[List[dict], Iterator[dict]], Optional[Union[dict, RequestOptions]]) -> MultipleResponse # noqa: E501

        safe = False
        if isinstance(request_options, dict) and "safe" in request_options:
            safe = request_options.pop("safe")

        tmp_index_name = self._create_temporary_name()
        responses = MultipleResponse()
        response = yield from self.copy_to_async(  # type: ignore
            tmp_index_name, {"scope": ["settings", "synonyms", "rules"]}
        )
        responses.push(response)

        if safe:
            responses.wait()

        tmp_client = SearchClient(self._transporter, self._config)
        tmp_index = SearchIndexAsync(
            tmp_client.init_index(tmp_index_name),
            self._transporter_async,
            self._config,
            tmp_index_name,
        )

        response = yield from tmp_index.save_objects_async(  # type: ignore
            objects, request_options
        )
        responses.push(response)

        if safe:
            responses.wait()

        response = yield from tmp_index.move_to_async(self._name)  # type: ignore
        responses.push(response)

        if safe:
            responses.wait()

        return responses

    def _sync(self):
        # type: () -> SearchIndex

        return self._search_index
