import pytest

from helpers import Factory
from helpers import create_client, create_index, IndexWithData


@pytest.fixture
def mcm_client():
    return create_client('ALGOLIA_APPLICATION_ID_MCM', 'ALGOLIA_API_KEY_MCM')


@pytest.fixture
def client():
    return create_client()


@pytest.fixture
def index(client):
    idx = create_index(client)
    yield idx
    client.delete_index(idx.index_name)  # Tear down


@pytest.fixture(scope='module')
def ro_index():
    idx = IndexWithData(create_client())
    yield idx
    idx.client.delete_index(idx.index_name)  # Tear down


@pytest.fixture
def rw_index():
    idx = IndexWithData(create_client())
    yield idx
    idx.client.delete_index(idx.index_name)  # Tear down


@pytest.fixture
def double_indexes():
    clt = create_client()
    factory = Factory()

    index1 = IndexWithData(clt, factory=factory)
    index2 = IndexWithData(clt, factory=factory)

    yield [index1, index2]

    # Tear down
    index1.client.delete_index(index1.index_name)
    index2.client.delete_index(index2.index_name)
