import math
import time

from typing import Optional, List, Union

from algoliasearch.configs import SearchConfig
from algoliasearch.exceptions import MissingObjectIdException
from algoliasearch.helpers import assert_object_id, build_raw_response_batch
from algoliasearch.http.request_options import RequestOptions
from algoliasearch.http.transporter import Transporter
from algoliasearch.http.verbs import Verbs
from algoliasearch.iterators import ObjectIterator
from algoliasearch.responses import Response, IndexingResponse


class SearchIndex(object):
    @property
    def app_id(self):
        return self.__config.app_id

    def __init__(self, transporter, config, name):
        # type: (Transporter, SearchConfig, str) -> None

        self.__transporter = transporter
        self.__config = config
        self.__name = name

    def save_object(self, obj, request_options=None):
        # type: (dict, Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

        return self.save_objects([obj], request_options)

    def save_objects(self, objects, request_options=None):
        # type: (List[dict], Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

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
                message += ". All objects must have an unique objectID (like a primary key) to be valid."  # noqa: E501
                message += "Algolia is also able to generate objectIDs automatically but *it's not recommended*."  # noqa: E501
                message += "To do it, use `save_objects(objects, {'autoGenerateObjectIDIfNotExist' => True})`."  # noqa: E501

                raise MissingObjectIdException(message, e.obj)

        return response

    def get_object(self, object_id, request_options=None):
        # type: (str, Optional[Union[dict, RequestOptions]]) -> dict

        return self.__transporter.read(
            Verbs.GET,
            '1/indexes/%s/%s' % (self.__name, object_id),
            {},
            request_options
        )

    def get_objects(self, object_ids, request_options=None):
        # type: (list, Optional[Union[dict, RequestOptions]]) -> dict

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

    def partial_update_objects(self, objects, request_options=None):
        # type: (list, Optional[Union[dict, RequestOptions]]) -> IndexingResponse # noqa: E501

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

    def get_task(self, task_id, request_options=None):
        # type: (int, Optional[Union[dict, RequestOptions]]) -> dict

        return self.__transporter.read(
            'GET',
            '1/indexes/%s/task/%s' % (self.__name, task_id),
            {},
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
            {},
            request_options
        )

        return IndexingResponse(self, [raw_response])

    def batch(self, data, request_options):
        raw_response = self.__batch(data, request_options)

        return IndexingResponse(self, [raw_response])

    def __chunk(self, action, objects, request_options,
                validate_object_id=True):
        # type: (str, list, Optional[Union[dict, RequestOptions]], bool) -> IndexingResponse # noqa: E501

        raw_responses = []
        batch = []
        batch_size = self.__config.batch_size
        for obj in objects:
            batch.append(obj)

            if len(batch) == batch_size:
                if validate_object_id:
                    assert_object_id(objects)

                data = build_raw_response_batch(action, objects)
                raw_responses.append(self.__batch(data, request_options))
                batch = []

        if len(batch):
            if validate_object_id:
                assert_object_id(objects)
            data = build_raw_response_batch(action, objects)
            raw_responses.append(self.__batch(data, request_options))

        return IndexingResponse(self, raw_responses)

    def __batch(self, data, request_options):
        # type: (dict, Optional[Union[dict, RequestOptions]]) -> dict

        return self.__transporter.write(
            Verbs.POST,
            '1/indexes/%s/batch' % self.__name,
            data,
            request_options
        )
