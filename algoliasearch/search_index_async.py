import asyncio
import math
from typing import Optional, Union, List, Iterator

from algoliasearch.configs import SearchConfig
from algoliasearch.helpers_async import _create_async_methods_in
from algoliasearch.helpers import endpoint
from algoliasearch.http.request_options import RequestOptions
from algoliasearch.http.serializer import SettingsDeserializer
from algoliasearch.http.transporter import Transporter
from algoliasearch.http.verbs import Verbs
from algoliasearch.responses import MultipleResponse
from algoliasearch.search_index import SearchIndex
from algoliasearch.iterators_async import (
    ObjectIteratorAsync,
    SynonymIteratorAsync,
    RuleIteratorAsync
)


class SearchIndexAsync(SearchIndex):

    def __init__(self, search_index, transporter, config, name):
        # type: (SearchIndex, Transporter, SearchConfig, str) -> None

        super(SearchIndexAsync, self).__init__(transporter, config, name)

        # First, we bind an async version of the method `wait_task` to the
        # method `wait_task` itself, to be used by async methods
        wait_task = self.__getattribute__('wait_task')
        self.__setattr__('wait_task', self.wait_task_async)

        # Then, we dynamically create {method}_async versions of all
        # public methods of the parent class, using a copy of
        # the current instance that contains an async `wait_task`
        _create_async_methods_in(self)

        # Finally, the re-bound the `wait_task` to his original definition
        self.__setattr__('wait_task', wait_task)

        self._search_index = search_index
        self._transporter = search_index._transporter
        self._transporter_async = transporter

    def wait_task_async(self, task_id, request_options=None):
        # type: (int, Optional[Union[dict, RequestOptions]]) -> None

        def async_():
            retries_count = 1

            while True:
                task = yield from self.get_task_async(task_id, request_options)

                if task['status'] == 'published':
                    break

                retries_count += 1
                factor = math.ceil(retries_count / 10)
                sleep_for = factor * self._config.wait_task_time_before_retry
                yield from asyncio.sleep(sleep_for / 1000000.0)

        asyncio.get_event_loop().run_until_complete(
            asyncio.coroutine(async_)()
        )

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

    @asyncio.coroutine
    def get_settings_async(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> dict # noqa: E501

        params = {'getVersion': 2}

        raw_response = yield from self._transporter_async.read(
            Verbs.GET,
            endpoint('1/indexes/%s/settings', self._name),
            params,
            request_options
        )

        return SettingsDeserializer.deserialize(raw_response)

    @asyncio.coroutine
    def replace_all_objects_async(self, objects, request_options=None):
        # type: (Union[List[dict], Iterator[dict]], Optional[Union[dict, RequestOptions]]) -> MultipleResponse # noqa: E501

        safe = False
        if isinstance(request_options, dict) \
                and 'safe' in request_options:
            safe = request_options.pop('safe')

        tmp_index_name = self._create_temporary_name()
        responses = MultipleResponse()
        response = yield from self.copy_to_async(tmp_index_name, {
            'scope': ['settings', 'synonyms', 'rules']
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

        response = yield from tmp_index.save_objects_async(objects,
                                                           request_options)
        responses.push(response)

        if safe:
            responses.wait()

        response = yield from tmp_index.move_to_async(self._name)
        responses.push(response)

        if safe:
            responses.wait()

        return responses
