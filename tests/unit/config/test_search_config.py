from algoliasearch.config.search_config import SearchConfig


def test_app_id():
    config = SearchConfig('foo', 'bar')
    assert config.app_id == 'foo'


def test_api_key():
    config = SearchConfig('foo', 'bar')
    assert config.api_key == 'bar'
