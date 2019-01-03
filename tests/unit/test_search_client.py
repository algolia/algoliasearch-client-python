from algoliasearch.search_client import SearchClient
from algoliasearch.search_index import SearchIndex
from algoliasearch.config.search_config import SearchConfig
from algoliasearch.http.transporter import Transporter
from algoliasearch.http.requester import Requester


def test_init():
    config = SearchConfig('foo', 'bar')
    transporter = Transporter(Requester, config)
    client = SearchClient(transporter, config)

    assert isinstance(client, SearchClient)


def test_init_index():
    config = SearchConfig('foo', 'bar')
    transporter = Transporter(Requester, config)
    client = SearchClient(transporter, config)

    index = client.init_index('foo')

    assert isinstance(index, SearchIndex)


def test_app_id_getter():
    client = SearchClient.create('foo', 'bar')

    assert client.app_id == 'foo'
