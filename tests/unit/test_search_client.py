from algoliasearch.search_client import SearchClient
from algoliasearch.search_index import SearchIndex
from algoliasearch.config.search_config import SearchConfig


def test_init():
    config = SearchConfig('foo', 'bar')
    client = SearchClient(config)
    index = client.init_index('foo')

    assert isinstance(index, SearchIndex)


def test_init_index():
    client = SearchClient.create('foo', 'bar')
    index = client.init_index('foo')

    assert isinstance(index, SearchIndex)


def test_app_id_getter():
    client = SearchClient.create('foo', 'bar')

    assert client.app_id == 'foo'
