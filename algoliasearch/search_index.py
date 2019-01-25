import copy
import math
import random
import string
import time

from typing import Optional, List, Union, Iterator

from algoliasearch.configs import SearchConfig
from algoliasearch.exceptions import MissingObjectIdException
from algoliasearch.helpers import assert_object_id, build_raw_response_batch
from algoliasearch.http.request_options import RequestOptions
from algoliasearch.http.transporter import Transporter
from algoliasearch.http.verbs import Verbs
from algoliasearch.iterators import ObjectIterator, SynonymIterator, \
    RuleIterator
from algoliasearch.responses import Response, IndexingResponse, \
    MultipleResponse


class SearchIndex(object):
    @property
    def app_id(self):
        return self.__config.app_id

    @property
    def name(self):
        return self.__name

    def __init__(self, transporter, config, name):
        # type: (Transporter, SearchConfig, str) -> None

        self.__transporter = transporter
        self.__config = config
        self.__name = name

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
            response = self.__chunk('addObject', objects, request_options,
                                    False)
        else:
            try:
                response = self.__chunk('updateObject', objects,
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

        tmp_index_name = self.__create_temporary_name()
        responses = MultipleResponse()
        responses.push(self.__copy_to(tmp_index_name, {
            'scope': ['settings', 'synonyms', 'rules']
        }))

        if safe:
            responses.wait()

        tmp_index = copy.copy(self)
        tmp_index.__name = tmp_index_name

        responses.push(tmp_index.save_objects(objects, request_options))

        if safe:
            responses.wait()

        responses.push(tmp_index.__move_to(self.__name))

        if safe:
            responses.wait()

        return responses

    def get_object(self, object_id, request_options=None):
        # type: (str, Optional[Union[dict, RequestOptions]]) -> dict

        return self.__transporter.read(
            Verbs.GET,
            '1/indexes/%s/%s' % (self.__name, object_id),
            None,
            request_options
        )

    def get_objects(self, object_ids, request_options=None):
        # type: (Iterator[int], Optional[Union[dict, RequestOptions]]) -> dict

        requests = []
        for object_id in object_ids:
            request = {'indexName': self.__name, 'objectID': str(object_id)}
            requests.append(request)

        return self.__transporter.read(
            Verbs.POST,
            '1/indexes/*/objects',
            {
                'requests': requests
            },
            request_options
        )

    def browse_objects(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> ObjectIterator

        return ObjectIterator(self.__transporter, self.__name, request_options)

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
            response = self.__chunk('partialUpdateObject', objects,
                                    request_options, False)
        else:
            response = self.__chunk('partialUpdateObjectNoCreate', objects,
                                    request_options)

        return response

    def delete_object(self, object_id, request_options=None):
        # type: (str, Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        return self.delete_objects([object_id], request_options)

    def delete_objects(self, object_ids, request_options=None):
        # type: (Union[List[str], Iterator[str]], Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        objects = list(
            map(lambda object_id: {'objectID': object_id}, object_ids))

        return self.__chunk('deleteObject', objects, request_options)

    def delete_by(self, filters, request_options=None):
        # type: (dict, Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        raw_response = self.__transporter.write(
            Verbs.POST,
            '1/indexes/%s/deleteByQuery' % self.__name,
            filters,
            request_options
        )

        return IndexingResponse(self, [raw_response])

    def clear_objects(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> IndexingResponse

        raw_response = self.__transporter.write(
            Verbs.POST,
            '1/indexes/%s/clear' % self.__name,
            None,
            request_options
        )

        return IndexingResponse(self, [raw_response])

    def set_settings(self, settings, request_options=None):
        # type: (dict, Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        raw_response = self.__transporter.write(
            Verbs.PUT,
            '1/indexes/%s/settings' % self.__name,
            settings,
            request_options
        )

        return IndexingResponse(self, [raw_response])

    def get_settings(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> dict # noqa: E501

        params = {'getVersion': 2}

        return self.__transporter.read(
            Verbs.GET,
            '1/indexes/%s/settings' % self.__name,
            params,
            request_options
        )

    def search(self, query, request_options=None):
        # type: (Optional[str], Optional[Union[dict, RequestOptions]]) -> dict # noqa: E501

        return self.__transporter.read(
            Verbs.POST,
            '1/indexes/%s/query' % self.__name,
            {
                'query': str(query)
            },
            request_options
        )

    def search_for_facet_value(self, facet_name, facet_query,
                               request_options=None):
        # type: (str, str, Optional[Union[dict, RequestOptions]]) -> dict # noqa: E501

        return self.__transporter.read(
            Verbs.POST,
            '1/indexes/%s/facets/%s/query' % (self.__name, facet_name),
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

        raw_response = self.__transporter.write(
            Verbs.POST,
            '1/indexes/%s/synonyms/batch' % self.__name,
            list(synonyms),
            request_options
        )

        return IndexingResponse(self, [raw_response])

    def replace_all_synonyms(self, synoyms, request_options=None):
        # type: (Union[List[dict], Iterator[dict]], Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        if request_options is None:
            request_options = RequestOptions.create(self.__config)
        elif isinstance(request_options, dict):
            request_options = RequestOptions.create(self.__config,
                                                    request_options)

        request_options['replaceExistingSynonyms'] = True

        return self.save_synonyms(list(synoyms), request_options)

    def get_synonym(self, object_id, request_options=None):
        # type: (str, Optional[Union[dict, RequestOptions]]) -> dict

        return self.__transporter.read(
            Verbs.GET,
            '1/indexes/%s/synonyms/%s' % (self.__name, object_id),
            None,
            request_options
        )

    def search_synonyms(self, query, request_options=None):
        # type: (str, Optional[Union[dict, RequestOptions]]) -> dict # noqa: E501

        return self.__transporter.read(
            Verbs.POST,
            '1/indexes/%s/synonyms/search' % self.__name,
            {
                'query': str(query)
            },
            request_options
        )

    def browse_synonyms(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> SynonymIterator

        return SynonymIterator(self.__transporter, self.__name,
                               request_options)

    def delete_synonym(self, object_id, request_options=None):
        # type: (str, Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        raw_response = self.__transporter.write(
            Verbs.DELETE,
            '1/indexes/%s/synonyms/%s' % (self.__name, object_id),
            None,
            request_options
        )

        return IndexingResponse(self, [raw_response])

    def clear_synonyms(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> IndexingResponse

        raw_response = self.__transporter.write(
            Verbs.POST,
            '1/indexes/%s/synonyms/clear' % self.__name,
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

        raw_response = self.__transporter.write(
            Verbs.POST,
            '1/indexes/%s/rules/batch' % self.__name,
            list(rules),
            request_options
        )

        return IndexingResponse(self, [raw_response])

    def replace_all_rules(self, rules, request_options=None):
        # type: (Union[List[dict], Iterator[dict]], Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        if request_options is None:
            request_options = RequestOptions.create(self.__config)
        elif isinstance(request_options, dict):
            request_options = RequestOptions.create(self.__config,
                                                    request_options)

        request_options.query_parameters['clearExistingRules'] = 1

        return self.save_rules(list(rules), request_options)

    def get_rule(self, object_id, request_options=None):
        # type: (str, Optional[Union[dict, RequestOptions]]) -> dict

        return self.__transporter.read(
            Verbs.GET,
            '1/indexes/%s/rules/%s' % (self.__name, object_id),
            None,
            request_options
        )

    def search_rules(self, query, request_options=None):
        # type: (str, Optional[Union[dict, RequestOptions]]) -> dict # noqa: E501

        return self.__transporter.read(
            Verbs.POST,
            '1/indexes/%s/rules/search' % self.__name,
            {
                'query': str(query)
            },
            request_options
        )

    def browse_rules(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> RuleIterator

        return RuleIterator(self.__transporter, self.__name,
                            request_options)

    def delete_rule(self, object_id, request_options=None):
        # type: (str, Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        raw_response = self.__transporter.write(
            Verbs.DELETE,
            '1/indexes/%s/rules/%s' % (self.__name, object_id),
            None,
            request_options
        )

        return IndexingResponse(self, [raw_response])

    def clear_rules(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> IndexingResponse

        raw_response = self.__transporter.write(
            Verbs.POST,
            '1/indexes/%s/rules/clear' % self.__name,
            None,
            request_options
        )

        return IndexingResponse(self, [raw_response])

    def get_task(self, task_id, request_options=None):
        # type: (int, Optional[Union[dict, RequestOptions]]) -> dict

        return self.__transporter.read(
            'GET',
            '1/indexes/%s/task/%s' % (self.__name, task_id),
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
            sleep_for = factor * self.__config.wait_task_time_before_retry
            time.sleep(sleep_for / 1000000.0)

    def delete(self, request_options=None):
        # type: (Optional[Union[dict, RequestOptions]]) -> Response

        raw_response = self.__transporter.write(
            Verbs.DELETE,
            '1/indexes/%s' % self.__name,
            None,
            request_options
        )

        return IndexingResponse(self, [raw_response])

    def batch(self, requests, request_options=None):
        # type: (Union[List[dict], Iterator[dict]], Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        raw_response = self.__raw_batch(requests, request_options)

        return IndexingResponse(self, [raw_response])

    def __chunk(self, action, objects, request_options,
                validate_object_id=True):
        # type: (str, Union[List[dict], Iterator[dict]], Optional[Union[dict, RequestOptions]], bool) -> IndexingResponse # noqa: E501

        raw_responses = []
        batch = []
        batch_size = self.__config.batch_size
        for obj in objects:
            batch.append(obj)

            if len(batch) == batch_size:
                if validate_object_id:
                    assert_object_id(objects)

                requests = build_raw_response_batch(action, objects)
                raw_responses.append(
                    self.__raw_batch(requests, request_options))
                batch = []

        if len(batch):
            if validate_object_id:
                assert_object_id(objects)
            requests = build_raw_response_batch(action, objects)
            raw_responses.append(self.__raw_batch(requests, request_options))

        return IndexingResponse(self, raw_responses)

    def __raw_batch(self, requests, request_options):
        # type: (Union[List[dict], Iterator[dict]], Optional[Union[dict, RequestOptions]]) -> dict # noqa: E501

        return self.__transporter.write(
            Verbs.POST,
            '1/indexes/%s/batch' % self.__name,
            {
                'requests': list(requests)
            },
            request_options
        )

    def __move_to(self, name, request_options=None):
        # type: (str, Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        raw_response = self.__transporter.write(
            Verbs.POST,
            '1/indexes/%s/operation' % self.__name,
            {
                'operation': 'move',
                'destination': name
            },
            request_options
        )

        return IndexingResponse(self, [raw_response])

    def __copy_to(self, name, request_options=None):
        # type: (str, Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        raw_response = self.__transporter.write(
            Verbs.POST,
            '1/indexes/%s/operation' % self.__name,
            {
                'operation': 'copy',
                'destination': name
            },
            request_options
        )

        return IndexingResponse(self, [raw_response])

    def __create_temporary_name(self):
        # type: () -> str

        letters = string.ascii_letters
        random_string = ''.join(random.choice(letters) for i in range(10))
        tmp_index_name = self.__name + '_tmp_' + random_string

        return tmp_index_name
