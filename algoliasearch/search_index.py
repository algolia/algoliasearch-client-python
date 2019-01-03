from typing import Optional

from algoliasearch.config.config import Config
from algoliasearch.http.request_options import RequestOptions
from algoliasearch.http.transporter import Transporter
from algoliasearch.http.verbs import Verbs


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
        # type: (dict, Optional[dict]) -> dict

        return self.__batch({
            'requests': [
                {
                    'action': 'addObject',
                    'body': obj
                }
            ],
        }, RequestOptions.create(self.__config, request_options))

    def get_object(self, object_id, request_options=None):
        # type: (str, Optional[dict]) -> dict

        return self.__transporter.read(
            Verbs.GET,
            '1/indexes/%s/%s' % (self.__name, object_id),
            RequestOptions.create(self.__config, request_options)
        )

    def __batch(self, data, request_options):
        # type: (dict, RequestOptions) -> dict

        return self.__transporter.write(
            Verbs.POST,
            '1/indexes/%s/batch' % self.__name,
            data,
            request_options
        )
