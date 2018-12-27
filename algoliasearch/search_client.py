from .search_index import SearchIndex
from .config.search_config import SearchConfig


class SearchClient:
    @property
    def app_id(self):
        return self.__config.app_id

    def __init__(self, search_config: SearchConfig):
        self.__config = search_config

    def init_index(self, name: str) -> SearchIndex:
        return SearchIndex(name)

    @staticmethod
    # @todo: Missing return hint here.
    def create(app_id: str, api_key: str):
        return SearchClient(SearchConfig(app_id, api_key))
