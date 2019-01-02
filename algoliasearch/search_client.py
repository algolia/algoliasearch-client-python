from .search_index import SearchIndex
from .config.search_config import SearchConfig
from .http.transporter import Transporter
from .http.requester import Requester


class SearchClient(object):
    @property
    def app_id(self):
        return self.__config.app_id

    def __init__(self, transporter: Transporter, search_config: SearchConfig):
        self.__transporter = transporter
        self.__config = search_config

    def init_index(self, name: str) -> SearchIndex:
        return SearchIndex(self.__transporter, self.__config, name)

    @staticmethod
    # @todo: Missing return hint here.
    def create(app_id: str, api_key: str):
        config = SearchConfig(app_id, api_key)
        transporter = Transporter(Requester, config)

        return SearchClient(transporter, config)
