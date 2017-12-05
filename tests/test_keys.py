from .helpers import wait_key, wait_missing_key


def test_list_user_keys(client):
    res = client.list_user_keys()
    assert 'keys' in res


def test_add_user_keys(client):
    keys = []

    res = client.add_user_key(['search'])
    assert len(res['key']) > 1
    keys.append(res['key'])

    res = client.add_user_key(['search'], max_queries_per_ip_per_hour=10)
    assert len(res['key']) > 1
    keys.append(res['key'])

    res = client.add_user_key(['search'], max_hits_per_query=5)
    assert len(res['key']) > 1
    keys.append(res['key'])

    res = client.add_user_key(['search'], validity=30)
    assert len(res['key']) > 1

    for key in keys:
        client.delete_user_key(key)


def test_get_user_key(client):
    res = client.add_user_key(['search'])
    key = res['key']
    wait_key(client, key)

    res = client.get_user_key_acl(key)
    assert res['value'] == key
    assert set(res['acl']) == set(['search'])

    client.delete_user_key(key)


def test_update_user_keys(client):
    keys = []

    for _ in range(3):
        res = client.add_user_key(['search'])
        keys.append(res['key'])

    for k in keys:
        wait_key(client, k)

    res = client.update_user_key(
        keys[0], ['addObject'], max_queries_per_ip_per_hour=5
    )
    assert res['key']
    wait_key(client, keys[0], lambda k: k['acl'] == ['addObject'])
    res = client.get_user_key_acl(keys[0])
    assert set(res['acl']) == set(['addObject'])
    assert res['maxQueriesPerIPPerHour'] == 5

    res = client.update_user_key(
        keys[1], ['deleteObject'], max_hits_per_query=10
    )
    assert res['key']

    wait_key(client, keys[1], lambda k: k['acl'] == ['deleteObject'])
    res = client.get_user_key_acl(keys[1])
    assert set(res['acl']) == set(['deleteObject'])
    assert res['maxHitsPerQuery'] == 10

    res = client.update_user_key(keys[2], ['settings', 'search'], validity=60)
    assert res['key']

    wait_key(client, keys[2], lambda k: set(k['acl']) == set(['settings', 'search']))
    res = client.get_user_key_acl(keys[2])
    assert set(res['acl']) == set(['settings', 'search'])
    assert 'validity' in res
    assert res['validity'] > 0

    for key in keys:
        client.delete_user_key(key)

def test_delete_user_keys(client):
    res = client.add_user_key(['search'])
    key = res['key']
    wait_key(client, res['key'])

    client.delete_user_key(key)
    wait_missing_key(client, res['key'])

    res = client.list_user_keys()
    res_keys = [elt['value'] for elt in res['keys']]
    assert key not in res_keys


def test_index_list_user_keys(ro_index):
    res = ro_index.list_user_keys()
    assert 'keys' in res


def test_index_add_user_keys(index):
    keys = []

    res = index.add_user_key(['search'])
    assert len(res['key']) > 1
    keys.append(res['key'])

    res = index.add_user_key(['search'], max_queries_per_ip_per_hour=10)
    assert len(res['key']) > 1
    keys.append(res['key'])

    res = index.add_user_key(['search'], max_hits_per_query=5)
    assert len(res['key']) > 1
    keys.append(res['key'])

    res = index.add_user_key(['search'], validity=30)
    assert len(res['key']) > 1

    for key in keys:
        index.delete_user_key(key)


def test_index_get_user_key(index):
    res = index.add_user_key(['search'])
    key = res['key']
    wait_key(index, res['key'])

    res = index.get_user_key_acl(key)
    assert res['value'] == key
    assert set(res['acl']) == set(['search'])

    index.delete_user_key(key)


def test_index_update_user_keys(index):
    keys = []

    for _ in range(3):
        res = index.add_user_key(['search'])
        keys.append(res['key'])

    for k in keys:
        wait_key(index, k)

    res = index.update_user_key(
        keys[0], ['addObject'], max_queries_per_ip_per_hour=5
    )
    assert res['key']
    wait_key(index, keys[0], lambda k: k['acl'] == ['addObject'])
    res = index.get_user_key_acl(keys[0])
    assert set(res['acl']) == set(['addObject'])
    assert res['maxQueriesPerIPPerHour'] == 5

    res = index.update_user_key(
        keys[1], ['deleteObject'], max_hits_per_query=10
    )
    assert res['key']
    wait_key(index, keys[1], lambda k: k['acl'] == ['deleteObject'])
    res = index.get_user_key_acl(keys[1])
    assert set(res['acl']) == set(['deleteObject'])
    assert res['maxHitsPerQuery'] == 10

    res = index.update_user_key(
        keys[2], ['settings', 'search'], validity=60
    )
    assert res['key']
    wait_key(index, keys[2], lambda k: set(k['acl']) == set(['search', 'settings']))
    res = index.get_user_key_acl(keys[2])
    assert set(res['acl']) == set(['settings', 'search'])
    assert 'validity' in res
    assert res['validity'] > 0

    for key in keys:
        index.delete_user_key(key)


def test_index_delete_user_keys(index):
    res = index.add_user_key(['search'])
    key = res['key']
    wait_key(index, res['key'])

    index.delete_user_key(key)
    wait_missing_key(index, res['key'])

    res = index.list_user_keys()
    res_keys = [elt['value'] for elt in res['keys']]
    assert key not in res_keys
