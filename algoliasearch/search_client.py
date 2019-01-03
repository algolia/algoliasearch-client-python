from .search_index import SearchIndex
from .config.search_config import SearchConfig
from .http.transporter import Transporter
from .http.requester import Requester


class SearchClient(object):
    @property
    def app_id(self):
        return self.__config.app_id

    def __init__(self, transporter, search_config):
        # type: (Transporter, SearchConfig) -> None

        self.__transporter = transporter
        self.__config = search_config

    def init_index(self, name):
        # type: (str) -> SearchIndex

        return SearchIndex(self.__transporter, self.__config, name)

    @staticmethod
    def create(app_id, api_key):
        # type: (str, str) -> SearchClient

        config = SearchConfig(app_id, api_key)
        requester = Requester()
        transporter = Transporter(requester, config)

        return SearchClient(transporter, config)
