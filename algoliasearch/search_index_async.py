import asyncio
import math
import types
from typing import Optional, Union, List, Iterator

from algoliasearch.configs import SearchConfig
from algoliasearch.helpers_async import _create_async_methods_in
from algoliasearch.helpers import endpoint
from algoliasearch.http.request_options import RequestOptions
from algoliasearch.http.serializer import SettingsDeserializer
from algoliasearch.http.transporter_async import TransporterAsync
from algoliasearch.http.verb import Verb
from algoliasearch.responses import MultipleResponse
from algoliasearch.search_index import SearchIndex
from algoliasearch.iterators_async import (
    ObjectIteratorAsync,
    SynonymIteratorAsync,
    RuleIteratorAsync
)


class SearchIndexAsync(SearchIndex):

    def __init__(self, search_index, transporter, config, name):
        # type: (SearchIndex, TransporterAsync, SearchConfig, str) -> None

        self._search_index = search_index
        self._transporter_async = transporter

        super(SearchIndexAsync, self).__init__(
            search_index._transporter,
            config,
            name
        )

        search_index = SearchIndex(transporter, config, name)
        search_index.__setattr__('_sync', self._sync)

        _create_async_methods_in(self, search_index)

    @asyncio.coroutine  # type: ignore
    def wait_task_async(self, task_id, request_options=None):  # type: ignore
        # type: (int, Optional[Union[dict, RequestOptions]]) -> None

        retries_count = 1

        while True:
            task = yield from self.get_task_async(  # type: ignore
                task_id,
                request_options
            )

            if task['status'] == 'published':
                break

            retries_count += 1
            factor = math.ceil(retries_count / 10)
            sleep_for = factor * self._config.wait_task_time_before_retry

            yield from asyncio.sleep(sleep_for / 1000000.0)

    def browse_objects_async(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> ObjectIteratorAsync

        return ObjectIteratorAsync(self._transporter_async, self._name,
                                   request_options)

    def browse_synonyms_async(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> SynonymIteratorAsync

        return SynonymIteratorAsync(self._transporter_async, self._name,
                                    request_options)

    def browse_rules_async(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> RuleIteratorAsync

        return RuleIteratorAsync(self._transporter_async, self._name,
                                 request_options)

    def get_settings_async(self, request_options=None):  # type: ignore
        # type: (Optional[Union[dict, RequestOptions]]) -> dict

        params = {'getVersion': 2}

        raw_response = yield from self._transporter_async.read(
            Verb.GET,
            endpoint('1/indexes/{}/settings', self._name),
            params,
            request_options
        )

        return SettingsDeserializer.deserialize(raw_response)

    def replace_all_objects_async(self, objects,  # type: ignore
                                  request_options=None):
        # type: (Union[List[dict], Iterator[dict]], Optional[Union[dict, RequestOptions]]) -> MultipleResponse # noqa: E501

        safe = False
        if isinstance(request_options, dict) \
                and 'safe' in request_options:
            safe = request_options.pop('safe')

        tmp_index_name = self._create_temporary_name()
        responses = MultipleResponse()
        response = yield from self.copy_to_async(  # type: ignore
            tmp_index_name,
            {
                'scope': ['settings',
                          'synonyms',
                          'rules']
            })
        responses.push(response)

        if safe:
            responses.wait()

        tmp_index = SearchIndexAsync(
            self._search_index,
            self._transporter_async,
            self._config,
            tmp_index_name
        )

        response = yield from tmp_index.save_objects_async(  # type: ignore
            objects,
            request_options
        )
        responses.push(response)

        if safe:
            responses.wait()

        response = yield from tmp_index.move_to_async(  # type: ignore
            self._name)
        responses.push(response)

        if safe:
            responses.wait()

        return responses

    def _sync(self):
        # type: () -> SearchIndex

        return self._search_index
