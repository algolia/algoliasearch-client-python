from .http.transporter import Transporter
from .config.search_config import SearchConfig
from .http.verbs import Verbs


class SearchIndex(object):
    @property
    def app_id(self):
        return self.__config.app_id

    def __init__(self, transporter: Transporter, config: SearchConfig, name: str) -> None:
        self.__transporter = transporter
        self.__config = config
        self.__name = name

    # Todo: Missing response object
    # Todo: Missing chunk
    # #type
    def save_object(self, obj) -> int:
        return self.__batch({
            'requests': [
                {
                    'action': 'addObject',
                    'body': obj
                }
            ]
        })

    # Todo: Missing response object
    # Todo: Missing chunk
    def get_object(self, object_id) -> dict:
        request_options = None

        return self.__transporter.read(
            Verbs.GET,
            '1/indexes/%s/%s' % (self.__name, object_id),
            request_options
        )

    def __batch(self, payload):
        request_options = None

        return self.__transporter.write(
            Verbs.POST,
            '1/indexes/%s/batch' % self.__name,
            payload,
            request_options
        )
