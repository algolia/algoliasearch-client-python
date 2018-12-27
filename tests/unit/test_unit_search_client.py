from algoliasearch.search_client import SearchClient
from algoliasearch.search_index import SearchIndex


def test_init_index():
    client = SearchClient()
    index = client.init_index('foo')

    assert isinstance(index, SearchIndex)
