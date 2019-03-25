import copy
import math
import random
import string
import time

from typing import Optional, List, Union, Iterator

from algoliasearch.configs import SearchConfig
from algoliasearch.exceptions import MissingObjectIdException
from algoliasearch.helpers import (
    assert_object_id,
    build_raw_response_batch,
    endpoint
)
from algoliasearch.http.request_options import RequestOptions
from algoliasearch.http.serializer import SettingsDeserializer
from algoliasearch.http.transporter import Transporter
from algoliasearch.http.verb import Verb
from algoliasearch.iterators import (
    ObjectIterator,
    SynonymIterator,
    RuleIterator
)
from algoliasearch.responses import (
    Response,
    IndexingResponse,
    MultipleResponse
)


class SearchIndex(object):
    @property
    def app_id(self):
        return self._config.app_id

    @property
    def name(self):
        return self._name

    def __init__(self, transporter, config, name):
        # type: (Transporter, SearchConfig, str) -> None

        self._transporter = transporter
        self._config = config
        self._name = name

    def save_object(self, obj, request_options=None):
        # type: (dict, Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        return self.save_objects([obj], request_options)

    def save_objects(self, objects, request_options=None):
        # type: (Union[List[dict], Iterator[dict]], Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        generate_object_id = False

        if isinstance(request_options, dict) \
                and 'autoGenerateObjectIDIfNotExist' in request_options:
            generate_object_id = request_options.pop(
                'autoGenerateObjectIDIfNotExist'
            )

        if generate_object_id:
            response = self._chunk('addObject', objects, request_options,
                                   False)
        else:
            try:
                response = self._chunk('updateObject', objects,
                                       request_options)
            except MissingObjectIdException as e:
                message = str(e)
                message += ". All objects must have an unique objectID " \
                           "(like a primary key) to be valid. " \
                           "Algolia is also able to generate objectIDs " \
                           "automatically but *it's not recommended*. " \
                           "To do it, use `save_objects(objects, " \
                           "{'autoGenerateObjectIDIfNotExist' => True})`."

                raise MissingObjectIdException(message, e.obj)

        return response

    def replace_all_objects(self, objects, request_options=None):
        # type: (Union[List[dict], Iterator[dict]], Optional[Union[dict, RequestOptions]]) -> MultipleResponse # noqa: E501

        safe = False
        if isinstance(request_options, dict) \
                and 'safe' in request_options:
            safe = request_options.pop('safe')

        tmp_index_name = self._create_temporary_name()
        responses = MultipleResponse()
        responses.push(self.copy_to(tmp_index_name, {
            'scope': ['settings', 'synonyms', 'rules']
        }))

        if safe:
            responses.wait()

        tmp_index = copy.copy(self)
        tmp_index._name = tmp_index_name

        responses.push(tmp_index.save_objects(objects, request_options))

        if safe:
            responses.wait()

        responses.push(tmp_index.move_to(self._name))

        if safe:
            responses.wait()

        return responses

    def get_object(self, object_id, request_options=None):
        # type: (str, Optional[Union[dict, RequestOptions]]) -> dict

        return self._transporter.read(
            Verb.GET,
            endpoint('1/indexes/{}/{}', self._name, object_id),
            None,
            request_options
        )

    def get_objects(self, object_ids, request_options=None):
        # type: (Iterator[str], Optional[Union[dict, RequestOptions]]) -> dict

        requests = []
        for object_id in object_ids:
            request = {'indexName': self._name, 'objectID': str(object_id)}
            requests.append(request)

        return self._transporter.read(
            Verb.POST,
            '1/indexes/*/objects',
            {
                'requests': requests
            },
            request_options
        )

    def browse_objects(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> ObjectIterator

        return ObjectIterator(self._transporter, self._name, request_options)

    def partial_update_object(self, obj, request_options=None):
        # type: (dict, Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        return self.partial_update_objects([obj], request_options)

    def partial_update_objects(self, objects, request_options=None):
        # type: (Union[List[dict], Iterator[dict]], Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        generate_object_id = False

        if isinstance(request_options, dict) \
                and 'createIfNotExists' in request_options:
            generate_object_id = request_options.pop(
                'createIfNotExists'
            )

        if generate_object_id:
            response = self._chunk('partialUpdateObject', objects,
                                   request_options, False)
        else:
            response = self._chunk('partialUpdateObjectNoCreate', objects,
                                   request_options)

        return response

    def delete_object(self, object_id, request_options=None):
        # type: (str, Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        return self.delete_objects([object_id], request_options)

    def delete_objects(self, object_ids, request_options=None):
        # type: (Union[List[str], Iterator[str]], Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        objects = list(
            map(lambda object_id: {'objectID': object_id}, object_ids))

        return self._chunk('deleteObject', objects, request_options)

    def delete_by(self, filters, request_options=None):
        # type: (dict, Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        raw_response = self._transporter.write(
            Verb.POST,
            endpoint('1/indexes/{}/deleteByQuery', self._name),
            filters,
            request_options
        )

        return IndexingResponse(self, [raw_response])

    def clear_objects(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> IndexingResponse

        raw_response = self._transporter.write(
            Verb.POST,
            endpoint('1/indexes/{}/clear', self._name),
            None,
            request_options
        )

        return IndexingResponse(self, [raw_response])

    def set_settings(self, settings, request_options=None):
        # type: (dict, Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        raw_response = self._transporter.write(
            Verb.PUT,
            endpoint('1/indexes/{}/settings', self._name),
            settings,
            request_options
        )

        return IndexingResponse(self, [raw_response])

    def get_settings(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> dict # noqa: E501

        params = {'getVersion': 2}

        raw_response = self._transporter.read(
            Verb.GET,
            endpoint('1/indexes/{}/settings', self._name),
            params,
            request_options
        )

        return SettingsDeserializer.deserialize(raw_response)

    def search(self, query, request_options=None):
        # type: (Optional[str], Optional[Union[dict, RequestOptions]]) -> dict # noqa: E501

        return self._transporter.read(
            Verb.POST,
            endpoint('1/indexes/{}/query', self._name),
            {
                'query': str(query)
            },
            request_options
        )

    def search_for_facet_values(self, facet_name, facet_query,
                                request_options=None):
        # type: (str, str, Optional[Union[dict, RequestOptions]]) -> dict # noqa: E501

        return self._transporter.read(
            Verb.POST,
            endpoint('1/indexes/{}/facets/{}/query', self._name, facet_name),
            {
                'facetQuery': facet_query
            },
            request_options
        )

    def save_synonym(self, synonym, request_options=None):
        # type: (dict, Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        return self.save_synonyms([synonym], request_options)

    def save_synonyms(self, synonyms, request_options=None):
        # type: (Union[List[dict], Iterator[dict]], Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        if not synonyms:
            return IndexingResponse(self, [])

        assert_object_id(synonyms)

        raw_response = self._transporter.write(
            Verb.POST,
            endpoint('1/indexes/{}/synonyms/batch', self._name),
            list(synonyms),
            request_options
        )

        return IndexingResponse(self, [raw_response])

    def replace_all_synonyms(self, synoyms, request_options=None):
        # type: (Union[List[dict], Iterator[dict]], Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        if request_options is None or isinstance(request_options, dict):
            request_options = RequestOptions.create(self._config,
                                                    request_options)

        request_options['replaceExistingSynonyms'] = True

        return self.save_synonyms(list(synoyms), request_options)

    def get_synonym(self, object_id, request_options=None):
        # type: (str, Optional[Union[dict, RequestOptions]]) -> dict

        return self._transporter.read(
            Verb.GET,
            endpoint('1/indexes/{}/synonyms/{}', self._name, object_id),
            None,
            request_options
        )

    def search_synonyms(self, query, request_options=None):
        # type: (str, Optional[Union[dict, RequestOptions]]) -> dict # noqa: E501

        return self._transporter.read(
            Verb.POST,
            endpoint('1/indexes/{}/synonyms/search', self._name),
            {
                'query': str(query)
            },
            request_options
        )

    def browse_synonyms(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> SynonymIterator

        return SynonymIterator(self._transporter, self._name,
                               request_options)

    def delete_synonym(self, object_id, request_options=None):
        # type: (str, Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        raw_response = self._transporter.write(
            Verb.DELETE,
            endpoint('1/indexes/{}/synonyms/{}', self._name, object_id),
            None,
            request_options
        )

        return IndexingResponse(self, [raw_response])

    def clear_synonyms(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> IndexingResponse

        raw_response = self._transporter.write(
            Verb.POST,
            endpoint('1/indexes/{}/synonyms/clear', self._name),
            None,
            request_options
        )

        return IndexingResponse(self, [raw_response])

    def save_rule(self, rule, request_options=None):
        # type: (dict, Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        return self.save_rules([rule], request_options)

    def save_rules(self, rules, request_options=None):
        # type: (Union[List[dict], Iterator[dict]], Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        if not rules:
            return IndexingResponse(self, [])

        assert_object_id(rules)

        raw_response = self._transporter.write(
            Verb.POST,
            endpoint('1/indexes/{}/rules/batch', self._name),
            list(rules),
            request_options
        )

        return IndexingResponse(self, [raw_response])

    def replace_all_rules(self, rules, request_options=None):
        # type: (Union[List[dict], Iterator[dict]], Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        if request_options is None or isinstance(request_options, dict):
            request_options = RequestOptions.create(self._config,
                                                    request_options)

        request_options.query_parameters['clearExistingRules'] = 1

        return self.save_rules(list(rules), request_options)

    def get_rule(self, object_id, request_options=None):
        # type: (str, Optional[Union[dict, RequestOptions]]) -> dict

        return self._transporter.read(
            Verb.GET,
            endpoint('1/indexes/{}/rules/{}', self._name, object_id),
            None,
            request_options
        )

    def search_rules(self, query, request_options=None):
        # type: (str, Optional[Union[dict, RequestOptions]]) -> dict # noqa: E501

        return self._transporter.read(
            Verb.POST,
            endpoint('1/indexes/{}/rules/search', self._name),
            {
                'query': str(query)
            },
            request_options
        )

    def browse_rules(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> RuleIterator

        return RuleIterator(self._transporter, self._name,
                            request_options)

    def delete_rule(self, object_id, request_options=None):
        # type: (str, Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        raw_response = self._transporter.write(
            Verb.DELETE,
            endpoint('1/indexes/{}/rules/{}', self._name, object_id),
            None,
            request_options
        )

        return IndexingResponse(self, [raw_response])

    def clear_rules(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> IndexingResponse

        raw_response = self._transporter.write(
            Verb.POST,
            endpoint('1/indexes/{}/rules/clear', self._name),
            None,
            request_options
        )

        return IndexingResponse(self, [raw_response])

    def get_task(self, task_id, request_options=None):
        # type: (int, Optional[Union[dict, RequestOptions]]) -> dict

        assert task_id, 'task_id cannot be empty.'

        return self._transporter.read(
            'GET',
            endpoint('1/indexes/{}/task/{}', self._name, task_id),
            None,
            request_options
        )

    def wait_task(self, task_id, request_options=None):
        # type: (int, Optional[Union[dict, RequestOptions]]) -> None

        retries_count = 1

        while True:
            task = self.get_task(task_id, request_options)
            if task['status'] == 'published':
                break

            retries_count += 1
            factor = math.ceil(retries_count / 10)
            sleep_for = factor * self._config.wait_task_time_before_retry
            time.sleep(sleep_for / 1000000.0)

    def delete(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> Response

        raw_response = self._transporter.write(
            Verb.DELETE,
            endpoint('1/indexes/{}', self._name),
            None,
            request_options
        )

        return IndexingResponse(self, [raw_response])

    def batch(self, requests, request_options=None):
        # type: (Union[List[dict], Iterator[dict]], Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        raw_response = self._raw_batch(requests, request_options)

        return IndexingResponse(self, [raw_response])

    def _chunk(self, action, objects, request_options,
               validate_object_id=True):
        # type: (str, Union[List[dict], Iterator[dict]], Optional[Union[dict, RequestOptions]], bool) -> IndexingResponse # noqa: E501

        raw_responses = []
        batch = []
        batch_size = self._config.batch_size
        for obj in objects:
            batch.append(obj)

            if len(batch) == batch_size:
                if validate_object_id:
                    assert_object_id(objects)

                requests = build_raw_response_batch(action, objects)
                raw_responses.append(
                    self._raw_batch(requests, request_options))
                batch = []

        if len(batch):
            if validate_object_id:
                assert_object_id(objects)
            requests = build_raw_response_batch(action, objects)
            raw_responses.append(self._raw_batch(requests, request_options))

        return IndexingResponse(self, raw_responses)

    def _raw_batch(self, requests, request_options):
        # type: (Union[List[dict], Iterator[dict]], Optional[Union[dict, RequestOptions]]) -> dict # noqa: E501

        return self._transporter.write(
            Verb.POST,
            endpoint('1/indexes/{}/batch', self._name),
            {
                'requests': list(requests)
            },
            request_options
        )

    def move_to(self, name, request_options=None):
        # type: (str, Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        raw_response = self._transporter.write(
            Verb.POST,
            endpoint('1/indexes/{}/operation', self._name),
            {
                'operation': 'move',
                'destination': name
            },
            request_options
        )

        return IndexingResponse(self, [raw_response])

    def copy_to(self, name, request_options=None):
        # type: (str, Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        raw_response = self._transporter.write(
            Verb.POST,
            endpoint('1/indexes/{}/operation', self._name),
            {
                'operation': 'copy',
                'destination': name
            },
            request_options
        )

        return IndexingResponse(self, [raw_response])

    def _create_temporary_name(self):
        # type: () -> str

        letters = string.ascii_letters
        random_string = ''.join(random.choice(letters) for i in range(10))
        tmp_index_name = '{}_tmp_{}'.format(self._name, random_string)

        return tmp_index_name

    def _sync(self):
        # type: () -> SearchIndex

        return self
