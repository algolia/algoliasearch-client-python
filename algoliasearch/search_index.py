import math
import time

from typing import Optional

from algoliasearch.config.config import Config
from algoliasearch.http.request_options import RequestOptions
from algoliasearch.http.transporter import Transporter
from algoliasearch.http.verbs import Verbs
from algoliasearch.responses import Response, IndexingResponse


class SearchIndex(object):
    @property
    def app_id(self):
        return self.__config.app_id

    def __init__(self, transporter, config, name):
        # type: (Transporter, Config, str) -> None

        self.__transporter = transporter
        self.__config = config
        self.__name = name

    def save_object(self, obj, request_options=None):
        # type: (dict, Optional[dict]) -> Response

        response = self.__batch({
            'requests': [
                {
                    'action': 'addObject',
                    'body': obj
                }
            ],
        }, RequestOptions.create(self.__config, request_options))

        return IndexingResponse(self, response)

    def get_object(self, object_id, request_options=None):
        # type: (str, Optional[dict]) -> dict

        return self.__transporter.read(
            Verbs.GET,
            '1/indexes/%s/%s' % (self.__name, object_id),
            RequestOptions.create(self.__config, request_options)
        )

    def get_task(self, task_id, request_options=None):
        # type:(int, Optional[dict]) -> dict

        return self.__transporter.read(
            'GET',
            '1/indexes/%s/task/%s' % (self.__name, task_id),
            RequestOptions.create(self.__config, request_options)
        )

    def wait_task(self, task_id, request_options=None):
        # type:(int, Optional[dict]) -> None

        retries_count = 1

        while True:
            task = self.get_task(task_id, request_options)
            if task['status'] == 'published':
                break

            retries_count += 1
            factor = math.ceil(retries_count / 10)
            sleep_for = factor * self.__config.wait_task_time_before_retry
            time.sleep(sleep_for / 1000000.0)

    def __batch(self, data, request_options):
        # type: (dict, RequestOptions) -> dict

        return self.__transporter.write(
            Verbs.POST,
            '1/indexes/%s/batch' % self.__name,
            data,
            request_options
        )
