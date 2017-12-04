from helpers import wait_key, wait_missing_key

def test_addObject(index):
    task = index.addObject({'name': 'Paris'}, 'a')
    index.waitTask(task['taskID'])
    results = index.search('')
    assert len(results['hits']) == 1
    assert results['hits'][0]['name'] == 'Paris'

    task = index.addObjects([
        {'name': 'Los Angeles'}, {'name': 'Los Gatos'}
    ])
    index.waitTask(task['taskID'])
    results = index.search('los')
    assert len(results['hits']) == 2

    task = index.partialUpdateObjects([{
        'name': 'San Francisco',
        'objectID': results['hits'][0]['objectID']
    }, {
        'name': 'San Marina',
        'objectID': results['hits'][1]['objectID']
    }])
    index.waitTask(task['taskID'])
    results = index.search('san', {
        "attributesToRetrieve": ["name"],
        "hitsPerPage": 20
    })
    assert len(results['hits']) == 2


def test_getObject(index):
    name = 'a'

    task = index.saveObject({
        "name": "San Francisco",
        "objectID": name
    })
    index.waitTask(task['taskID'])
    obj = index.getObject(name, 'name')
    assert obj['name'] == 'San Francisco'

    task = index.partialUpdateObject({
        "name": "San Diego",
        "objectID": name
    })
    index.waitTask(task['taskID'])
    obj = index.getObject(name)
    assert obj['name'] == 'San Diego'

    task = index.saveObjects([{
        "name": "Los Angeles",
        "objectID": name
    }])
    index.waitTask(task['taskID'])
    obj = index.getObject(name)
    assert obj['name'] == 'Los Angeles'


def test_getObjects(ro_index):
    results = ro_index.getObjects(ro_index.ids)
    names = [elt['name'] for elt in ro_index.data]
    for result in results['results']:
        assert result['name'] in names


def test_deleteObject(rw_index):
    res = rw_index.deleteObject(rw_index.ids[0])
    rw_index.waitTask(res['taskID'])
    results = rw_index.search('')
    ids = [hit['objectID'] for hit in results['hits']]
    assert rw_index.ids[0] not in ids
    for objid in rw_index.ids[1:]:
        assert objid in ids


def test_listIndexes(double_indexes):
    res = double_indexes[0].client.listIndexes()
    names = [item['name'] for item in res['items']]
    for index in double_indexes:
        assert index.index_name in names


def test_clearIndex(rw_index):
    results = rw_index.search('')
    assert len(results['hits']) == len(rw_index.ids)
    task = rw_index.clearIndex()
    rw_index.waitTask(task['taskID'])
    results = rw_index.search('')
    assert not results['hits']


def test_copy(double_indexes):
    index1 = double_indexes[0]
    index2 = double_indexes[1]
    client = index1.client

    task = client.copyIndex(index1.index_name, index2.index_name)
    index1.waitTask(task['taskID'])
    res = [index.search('') for index in double_indexes]
    assert res[0]['hits'] == res[1]['hits']


def test_move(double_indexes):
    index1 = double_indexes[0]
    index2 = double_indexes[1]
    client = index1.client

    task = client.moveIndex(index1.index_name, index2.index_name)
    index1.waitTask(task['taskID'])

    res = client.listIndexes()
    names = [item['name'] for item in res['items']]
    assert index1.index_name not in names

    res = index2.search('')
    ids = [hit['objectID'] for hit in res['hits']]
    assert sorted(ids) == sorted(index1.ids)


def test_log(ro_index):
    res = ro_index.client.getLogs()
    assert res['logs']


def test_deleteByQuery(rw_index):
    task = rw_index.deleteByQuery(rw_index.data[2]['name'][0])
    rw_index.waitTask(task['taskID'])

    res = rw_index.search('')
    assert res['nbHits'] < 5


def test_user_key(rw_index):
    new_key = rw_index.addUserKey(['search'])
    wait_key(rw_index, new_key['key'])
    assert new_key['key']

    res = rw_index.listUserKeys()
    assert new_key['key'] in [key['value'] for key in res['keys']]

    key = rw_index.getUserKeyACL(new_key['key'])
    assert key['acl'][0] == 'search'

    rw_index.deleteUserKey(new_key['key'])
    wait_missing_key(rw_index, new_key['key'])
    res = rw_index.listUserKeys()
    assert new_key['key'] not in [key['value'] for key in res['keys']]


def test_settings(index):
    task = index.setSettings({'attributesToRetrieve': ['name']})
    index.waitTask(task['taskID'])
    settings = index.getSettings()
    assert len(settings['attributesToRetrieve']) == 1
    assert settings['attributesToRetrieve'][0] == 'name'


def test_multipleQueries(ro_index):
    results = ro_index.client.multipleQueries([{
        "indexName": ro_index.index_name,
        "query": ""
    }])

    assert len(results['results']) == 1

    ids = [hit['objectID'] for hit in results['results'][0]['hits']]
    assert len(ids) == 5

    for objid in ro_index.ids:
        assert objid in ids


def test_disjunctive_faceting(index):
    index.setSettings(
        {"attributesForFacetting": ['city', 'stars', 'facilities']})
    task = index.addObjects([{
        "name": 'Hotel A',
        "stars": '*',
        "facilities": ['wifi', 'bath', 'spa'],
        "city": 'Paris'
    }, {
        "name": 'Hotel B',
        "stars": '*',
        "facilities": ['wifi'],
        "city": 'Paris'
    }, {
        "name": 'Hotel C',
        "stars": '**',
        "facilities": ['bath'],
        "city": 'San Francisco'
    }, {
        "name": 'Hotel D',
        "stars": '****',
        "facilities": ['spa'],
        "city": 'Paris'
    }, {
        "name": 'Hotel E',
        "stars": '****',
        "facilities": ['spa'],
        "city": 'New York'
    }])
    index.waitTask(task['taskID'])

    answer = index.searchDisjunctiveFaceting(
        'h', ['stars', 'facilities'], {"facets": "city"}
    )
    assert answer['nbHits'] == 5
    assert len(answer['facets']) == 1
    assert len(answer['disjunctiveFacets']) == 2

    answer = index.searchDisjunctiveFaceting(
        'h', ['stars', 'facilities'],
        {"facets": "city"}, {"stars": ["*"]}
    )
    assert answer['nbHits'] == 2
    assert len(answer['facets']) == 1
    assert len(answer['disjunctiveFacets']) == 2
    assert answer['disjunctiveFacets']['stars']['*'] == 2
    assert answer['disjunctiveFacets']['stars']['**'] == 1
    assert answer['disjunctiveFacets']['stars']['****'] == 2

    answer = index.searchDisjunctiveFaceting(
        'h', ['stars', 'facilities'],
        {"facets": "city"}, {"stars": ['*'], "city": ["Paris"]}
    )
    assert answer['nbHits'] == 2
    assert len(answer['facets']) == 1
    assert len(answer['disjunctiveFacets']) == 2
    assert answer['disjunctiveFacets']['stars']['*'] == 2
    assert answer['disjunctiveFacets']['stars']['****'] == 1

    answer = index.searchDisjunctiveFaceting(
        'h', ['stars', 'facilities'],
        {"facets": "city"}, {"stars": ['*', '****'], "city": ["Paris"]}
    )
    assert answer['nbHits'] == 3
    assert len(answer['facets']) == 1
    assert len(answer['disjunctiveFacets']) == 2
    assert answer['disjunctiveFacets']['stars']['*'] == 2
    assert answer['disjunctiveFacets']['stars']['****'] == 1


def test_attributeToRetrieve(ro_index):
    hits = ro_index.search('', {
        'attributesToRetrieve': ['name', 'email']
    })['hits']

    assert len(hits) == 5
    assert 'phone' not in hits[0]

    names = [hit['name'] for hit in hits]
    emails = [hit['email'] for hit in hits]
    for elt in ro_index.data:
        assert elt['name'] in names
        assert elt['email'] in emails

    hits = ro_index.search('', {
        'attributesToRetrieve': "name,email"
    })['hits']

    assert len(hits) == 5
    assert 'phone' not in hits[0]

    names = [hit['name'] for hit in hits]
    emails = [hit['email'] for hit in hits]
    for elt in ro_index.data:
        assert elt['name'] in names
        assert elt['email'] in emails
