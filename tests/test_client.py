import os
import time

from algoliasearch.client import RequestOptions, MAX_API_KEY_LENGTH, Client
from algoliasearch.helpers import AlgoliaException
from fake_session import FakeSession
from helpers import Factory, check_credentials


def test_request_options(client):
    options = {'forwardedFor': 'blabla', 'hitsPerPage': 40}

    expected_headers = client._transport.headers.copy()
    expected_headers.update({'X-Forwarded-For': 'blabla'})

    fake_session = FakeSession(expected_headers, {'hitsPerPage': 40})

    old_session = client._transport.session
    client._transport.session = fake_session
    client.is_alive(RequestOptions(options))
    client._transport.session = old_session


def test_rate_limit_forward(client):
    headers_rate_limit = {
        'X-Forwarded-For': '127.0.0.1',
        'X-Forwarded-API-Key': 'userSearchKey'
    }

    client.enable_rate_limit_forward('127.0.0.1', 'userSearchKey')
    for key in headers_rate_limit:
        assert headers_rate_limit[key] == client.headers[key]

    client.disable_rate_limit_forward()
    for key in headers_rate_limit:
        assert key not in client.headers


def test_set_end_user_ip(client):
    client.set_end_user_ip('192.168.0.1')
    assert 'X-Forwarded-For' in client.headers
    assert client.headers['X-Forwarded-For'] == '192.168.0.1'


def test_set_extra_headers(client):
    client.set_extra_headers(Private='on')
    assert 'Private' in client.headers
    assert client.headers['Private'] == 'on'

    client.set_extra_headers(**{
        'X-User': '223254',
        'X-Privacy-Settings': 'NSA-Free'
    })

    assert 'X-User' in client.headers
    assert client.headers['X-User'] == '223254'
    assert 'X-Privacy-Settings' in client.headers
    assert client.headers['X-Privacy-Settings'] == 'NSA-Free'


def test_get_logs(client):
    res = client.get_logs(length=1)
    assert len(res['logs']) == 1

    res = client.get_logs(length=3)
    assert len(res['logs']) == 3


def test_change_api_key(client):
    client.api_key = 'your_api_key'
    assert client._api_key == 'your_api_key'
    assert client.headers['X-Algolia-API-Key'] == 'your_api_key'


def test_change_api_key_too_long(client):
    api_key = 'a' * (MAX_API_KEY_LENGTH + 1)
    client.api_key = api_key
    assert client._api_key == api_key
    assert 'X-Algolia-API-Key' not in client.headers

def test_change_api_key_max_length(client):
    api_key = 'a' * MAX_API_KEY_LENGTH
    client.api_key = api_key
    assert client._api_key == api_key
    assert client.headers['X-Algolia-API-Key'] == api_key


def test_subclassing_client():
    class SubClient(Client):
        def __init__(self, user_name, *args, **kwargs):
            super(SubClient, self).__init__(*args, **kwargs)
            self._user_name = user_name
            self.set_extra_headers(**{'X-User': user_name})

        @property
        def user_name(self):
            return self._user_name

    sub_client = SubClient('algolia', 'myAppID', 'myApiKey')
    assert sub_client.app_id == 'myAppID'
    assert sub_client.api_key == 'myApiKey'
    assert sub_client.user_name == 'algolia'
    assert 'X-User' in sub_client.headers
    assert sub_client.headers['X-User'] == 'algolia'


def test_dns_timeout():
    check_credentials()
    app_id = os.environ['ALGOLIA_APPLICATION_ID']

    hosts = ['algolia.biz']
    client = Client(app_id, os.environ['ALGOLIA_API_KEY'], hosts)

    client.timeout = (5, 2)
    client.search_timeout = (5, 2)

    now = time.time()
    try:
        client.list_indexes()
        assert False
    except AlgoliaException:
        pass

    assert time.time() < now + 6


def test_dns_timeout_hard():
    check_credentials()
    app_id = os.environ['ALGOLIA_APPLICATION_ID']

    hosts = ['algolia.biz', '%s-dsn.algolia.net' % app_id]
    client = Client(app_id, os.environ['ALGOLIA_API_KEY'], hosts)

    now = time.time()
    for _ in range(10):
        client.list_indexes()

    assert time.time() < now + 6


def test_is_alive(client):
    res = client.is_alive()
    assert 'message' in res


def test_list_indexes(double_indexes):
    client = double_indexes[0].client

    res = client.list_indexes()
    names = [item['name'] for item in res['items']]
    for index in double_indexes:
        assert index.index_name in names


def test_clear_index(double_indexes):
    index1 = double_indexes[0]
    index2 = double_indexes[1]

    task = index1.clear_index()
    index1.wait_task(task['taskID'])
    res = index1.search('')
    assert res['nbHits'] == 0

    res = index2.search('', {'hitsPerPage': 0})
    assert res['nbHits'] == 5


def test_copy(double_indexes):
    index1 = double_indexes[0]
    index2 = double_indexes[1]

    task = index1.client.copy_index(index1.index_name, index2.index_name)
    index1.wait_task(task['taskID'])

    res = index1.client.list_indexes()
    res_names = [elt['name'] for elt in res['items']]
    for name in [index1.index_name, index2.index_name]:
        assert name in res_names

    res = [index.search('') for index in double_indexes]
    assert res[0]['hits'] == res[1]['hits']


def test_move(double_indexes):
    index1 = double_indexes[0]
    index2 = double_indexes[1]

    task = index1.client.move_index(index1.index_name, index2.index_name)
    index1.wait_task(task['taskID'])

    res = index1.client.list_indexes()
    res_names = [elt['name'] for elt in res['items']]
    assert index1.index_name not in res_names
    assert index2.index_name in res_names

    res = index2.search('', {'attributesToRetrieve': ['objectID']})
    res_ids = [elt['objectID'] for elt in res['hits']]
    for elt in res_ids:
        assert elt in index1.ids
        assert elt not in index2.ids


def test_delete_index(double_indexes):
    index1 = double_indexes[0]
    index2 = double_indexes[1]

    task = index1.client.delete_index(index1.index_name)
    index1.wait_task(task['taskID'])

    res = index1.client.list_indexes()
    res_names = [elt['name'] for elt in res['items']]

    assert index1.index_name not in res_names
    assert index2.index_name in res_names


def test_batch_multiple_indexes(double_indexes):
    factory = Factory()
    index1 = double_indexes[0]
    index2 = double_indexes[1]

    params = {'hitsPerPage': 0}
    requests = [
        {
            'action': 'addObject',
            'indexName': index1.index_name,
            'body': factory.contacts()
        }, {
            'action': 'addObject',
            'indexName': index2.index_name,
            'body': factory.contacts()
        }, {
            'action': 'addObject',
            'indexName': index1.index_name,
            'body': factory.contacts()
        }
    ]

    task = index1.client.batch({'requests': requests})

    for index in double_indexes:
        index.wait_task(task['taskID'][index.index_name])

    res = index1.search('', params)
    assert res['nbHits'] == 7
    res = index2.search('', params)
    assert res['nbHits'] == 6

    requests = [
        {
            'action': 'deleteObject',
            'indexName': index1.index_name,
            'objectID': index1.ids[2]
        }, {
            'action': 'deleteObject',
            'indexName': index2.index_name,
            'objectID': index2.ids[1]
        }, {
            'action': 'deleteObject',
            'indexName': index2.index_name,
            'objectID': index2.ids[0]
        }, {
            'action': 'deleteObject',
            'indexName': index1.index_name,
            'objectID': index1.ids[3]
        }, {
            'action': 'deleteObject',
            'indexName': index2.index_name,
            'objectID': index2.ids[2]
        }
    ]

    task = index1.client.batch(requests)
    for index in double_indexes:
        index.wait_task(task['taskID'][index.index_name])

    res = index1.search('', params)
    assert res['nbHits'] == 5
    res = index2.search('', params)
    assert res['nbHits'] == 3

def test_multiple_queries(double_indexes):
    index1 = double_indexes[0]
    index2 = double_indexes[1]

    res = index1.client.multiple_queries([
        {'indexName': index1.index_name, 'query': ''},
        {'indexName': index2.index_name, 'query': ''}
    ])

    assert len(res['results']) == 2
    for i, res in enumerate(res['results']):
        res_ids = [elt['objectID'] for elt in res['hits']]
        for elt in double_indexes[i].ids:
            assert elt in res_ids
