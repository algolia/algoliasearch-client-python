from .search_index import SearchIndex


class SearchClient:
    def init_index(self, name: str) -> SearchIndex:
        return SearchIndex(name)
