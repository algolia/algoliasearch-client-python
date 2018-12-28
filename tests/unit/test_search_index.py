from algoliasearch.search_client import SearchClient
from algoliasearch.search_index import SearchIndex
from algoliasearch.config.search_config import SearchConfig
from algoliasearch.http.transporter import Transporter
from algoliasearch.http.requester import Requester

def test_init():
    config = SearchConfig('foo', 'bar')
    transporter = Transporter(Requester, config)
    index = SearchIndex(transporter, config, 'foo')

    assert isinstance(index, SearchIndex)

def test_app_id_getter():
    index = SearchClient.create('foo', 'bar').init_index('index')

    assert index.app_id == 'foo'
