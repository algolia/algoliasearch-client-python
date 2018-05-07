import calendar
import os
import re
from datetime import datetime
from decimal import Decimal

from algoliasearch.client import MAX_API_KEY_LENGTH
from algoliasearch.helpers import AlgoliaException

from .helpers import Factory, rule_stub


def test_add_object(index):
    factory = Factory()
    obj = factory.contacts()
    task = index.add_object(obj)
    index.wait_task(task['taskID'])

    res = index.get_object(task['objectID'])
    del res['objectID']
    assert res == obj


def test_add_object_with_objectID(index):
    factory = Factory()
    obj = factory.with_objectids('101')
    task = index.add_object(obj, obj['objectID'])
    index.wait_task(task['taskID'])

    res = index.get_object(obj['objectID'])
    assert res == obj


def test_add_objects(index):
    factory = Factory()
    objs = factory.contacts(5)
    task = index.add_objects(objs)
    index.wait_task(task['taskID'])

    res = index.get_objects(task['objectIDs'])
    assert len(res['results']) == 5

    for obj, obj_res in zip(objs, res['results']):
        del obj_res['objectID']
        assert obj == obj_res


def test_save_object(index):
    factory = Factory()
    obj = factory.with_objectids(4242)
    task = index.save_object(obj)
    index.wait_task(task['taskID'])

    res = index.get_object(obj['objectID'])
    obj['objectID'] = '4242'  # The backends always returns str(objectID)
    assert obj == res


def test_save_objects(index):
    factory = Factory()
    ids = factory.objectids(5)
    objs = factory.with_objectids(ids)
    task = index.save_objects(objs)
    index.wait_task(task['taskID'])

    res = index.get_objects(ids)
    for obj, obj_res in zip(objs, res['results']):
        assert obj == obj_res


def test_encode_decimal(index):
    value = Decimal('3.14')
    task = index.add_object({'pi': value})
    index.wait_task(task['taskID'])

    res = index.get_object(task['objectID'])
    assert res['pi'] == float(value)


def test_encode_datetime(index):
    value = datetime.now()
    task = index.add_object({'now': value})
    index.wait_task(task['taskID'])

    res = index.get_object(task['objectID'])
    assert res['now'] == calendar.timegm(value.utctimetuple())


def test_synonyms(index):
    index.add_object({'name': '589 Howard St., San Francisco'})
    task = index.batch_synonyms([
        {'objectID': 'city', 'type': 'synonym',
         'synonyms': ['San Francisco', 'SF']},
        {'objectID': 'street', 'type': 'altCorrection1',
         'word': 'Street', 'corrections': ['St']}
    ])

    index.wait_task(task['taskID'])
    task = index.get_synonym("city")
    assert task['objectID'] == 'city'

    task = index.search('Howard Street SF')
    assert int(task['nbHits'] == 1)

    task = index.delete_synonym('street')
    index.wait_task(task['taskID'])
    task = index.search_synonyms('', ['synonym'], 0, 5)
    assert int(task['nbHits']) == 1

    task = index.clear_synonyms()
    index.wait_task(task['taskID'])
    task = index.search_synonyms('', hits_per_page=5)
    assert int(task['nbHits']) == 0


def test_iter_synonyms(index):
    synonyms = [{
        'objectID': 'city',
        'type': 'synonym',
        'synonyms': ['San Francisco', 'SF']
    }, {
        'objectID': 'street',
        'type': 'altCorrection1',
        'word': 'Street', 'corrections': ['St']
    }]

    task = index.batch_synonyms(synonyms)
    index.wait_task(task['taskID'])

    res = list(index.iter_synonyms(hits_per_page=1))
    assert len(res) == 2

    for synonym in synonyms:
        assert synonym in res


def test_iter_rules(index):
    rules = [
        rule_stub('rule1'),
        rule_stub('rule2')
    ]

    task = index.batch_rules(rules)
    index.wait_task(task['taskID'])

    res = list(index.iter_rules(hits_per_page=1))
    assert len(res) == 2

    for rule in rules:
        assert rule in res


def test_facet_search(index):
    settings = {'attributesForFacetting': ['searchable(series)', 'kind']}
    objects = [{
        'objectID': '1',
        'name': 'Snoopy',
        'kind': ['dog', 'animal'],
        'born': 1950,
        'series': 'Peanuts'
    }, {
        'objectID': '2',
        'name': 'Woodstock',
        'kind': ['bird', 'animal'],
        'born': 1960,
        'series': 'Peanuts'
    }, {
        'objectID': '3',
        'name': 'Charlie Brown',
        'kind': ['human'],
        'born': 1950,
        'series': 'Peanuts'
    }, {
        'objectID': '4',
        'name': 'Hobbes',
        'kind': ['tiger', 'animal', 'teddy'],
        'born': 1985,
        'series': 'Calvin & Hobbes'
    }, {
        'objectID': '5',
        'name': 'Calvin',
        'kind': ['human'],
        'born': 1985,
        'series': 'Calvin & Hobbes'
    }]

    index.set_settings(settings)
    task = index.add_objects(objects)
    index.wait_task(task['taskID'])

    # Straightforward search.
    facet_hits = index.search_facet('series', 'Hobb')['facetHits']
    assert len(facet_hits) == 1
    assert facet_hits[0]['value'] == 'Calvin & Hobbes'
    assert facet_hits[0]['count'] == 2

    # Using an addition query to restrict search.
    query = {'facetFilters': 'kind:animal', 'numericFilters': 'born >= 1955'}
    facet_hits = index.search_facet('series', 'Peanutz', query)['facetHits']
    assert facet_hits[0]['value'] == 'Peanuts'
    assert facet_hits[0]['count'] == 1


def test_save_and_get_rule(index):
    rule = rule_stub()
    res = index.save_rule(rule)
    index.wait_task(res['taskID'])
    assert index.read_rule('my-rule') == rule


def test_empty_objectID_for_rule_should_raise_exception(index):
    rule = rule_stub()
    rule['objectID'] = ''

    try:
        index.save_rule(rule)
    except AlgoliaException:
        return

    # We should not be able to save a rule with an empty objectID.
    assert False

def test_delete_rule(index):
    rule = rule_stub()
    res = index.save_rule(rule)
    index.wait_task(res['taskID'])

    res = index.delete_rule('my-rule')
    index.wait_task(res['taskID'])

    try:
        index.read_rule('my-rule')
    except AlgoliaException:
        return

    # We should not be able to access a deleted objectID.
    assert False


def test_search_rules(index):
    rule = rule_stub()
    rule2 = rule_stub('my-second-rule')

    res = index.save_rule(rule)
    index.wait_task(res['taskID'])

    res = index.save_rule(rule2)
    index.wait_task(res['taskID'])

    rules = index.search_rules()
    assert rules['nbHits'] == 2


def test_batch_and_clear_rules(index):
    rule = rule_stub()
    rule2 = rule_stub('my-second-rule')

    res = index.batch_rules([rule, rule2])
    index.wait_task(res['taskID'])

    assert index.read_rule('my-rule') == rule
    assert index.read_rule('my-second-rule') == rule2

    res = index.clear_rules()
    index.wait_task(res['taskID'])

    rules = index.search_rules()
    assert rules['nbHits'] == 0


def test_batch_and_clear_existing(index):
    rule = rule_stub()
    rule2 = rule_stub('my-second-rule')
    rule3 = rule_stub('my-third-rule')
    rule4 = rule_stub('my-fourth-rule')

    res = index.batch_rules([rule, rule2, rule3, rule4])
    index.wait_task(res['taskID'])

    res = index.batch_rules([rule3, rule4], False, True)
    index.wait_task(res['taskID'])

    rules = index.search_rules()
    assert rules['nbHits'] == 2

    del rules['hits'][0]['_highlightResult']
    del rules['hits'][1]['_highlightResult']

    assert rules['hits'] == [rule3, rule4]  # alphabetical ordering of objectID

def test_settings(ro_index):
    task = ro_index.set_settings({
        'attributesToHighlight': ['name']
    })
    ro_index.wait_task(task['taskID'])

    res = ro_index.get_settings()
    assert res['attributesToHighlight'] == ['name']


def test_get_object(ro_index):
    res = ro_index.get_object(ro_index.ids[3])
    del res['objectID']
    assert ro_index.data[3] == res

    res = ro_index.get_object(ro_index.ids[0])
    del res['objectID']
    assert ro_index.data[0] == res

    res = ro_index.get_object(ro_index.ids[4])
    del res['objectID']
    assert ro_index.data[4] == res


def test_get_object_with_attributes_to_retrieve(ro_index):
    res = ro_index.get_object(ro_index.ids[3], attributes_to_retrieve=['name', 'email'])
    assert ro_index.data[3]['name'] == res['name']
    assert ro_index.data[3]['email'] == res['email']
    assert 'phone' not in res
    assert 'city' not in res
    assert 'country'not in res

    res = ro_index.get_object(ro_index.ids[0], attributes_to_retrieve='city')
    assert 'name' not in res
    assert 'email' not in res
    assert 'phone' not in res
    assert ro_index.data[0]['city'] == res['city']
    assert 'country' not in res

    res = ro_index.get_object(ro_index.ids[0], attributes_to_retrieve='objectID')
    assert 'name' not in res
    assert 'email' not in res
    assert 'phone' not in res
    assert 'city' not in res
    assert 'country' not in res


def test_get_objects(ro_index):
    res = ro_index.get_objects(ro_index.ids[1:3])
    for obj, obj_res in zip(ro_index.data[1:3], res['results']):
        del obj_res['objectID']
        assert obj == obj_res

    res = ro_index.get_objects([ro_index.ids[3], ro_index.ids[0], ro_index.ids[2]])
    assert len(res['results']) == 3

    for result in res['results']:
        del result['objectID']

    assert ro_index.data[3] == res['results'][0]
    assert ro_index.data[0] == res['results'][1]
    assert ro_index.data[2] == res['results'][2]


def test_get_objects_with_attributes_to_retrieve(ro_index):
    res = ro_index.get_objects(ro_index.ids[1:3], attributes_to_retrieve=['name', 'email'])
    for obj, obj_res in zip(ro_index.data[1:3], res['results']):
        assert obj['name'] == obj_res['name']
        assert obj['email'] == obj_res['email']
        assert 'phone' not in obj_res
        assert 'city' not in obj_res
        assert 'country' not in obj_res


def test_browse(ro_index):
    res = ro_index.browse(page=0, hits_per_page=2)
    assert res['page'] == 0
    assert res['nbHits'] == 5
    assert res['hitsPerPage'] == 2

    for i in range(5):
        res = ro_index.browse(page=i, hits_per_page=1)
        assert res['hits'][0]['objectID'] in ro_index.ids


def test_browse_all(ro_index):
    params = {
        'hitsPerPage': 2,
        'attributesToRetrieve': ['objectID']
    }

    res_ids = []
    it = ro_index.browse_all(params)
    for record in it:
        assert len(record.keys()) == 1
        assert 'objectID' in record
        res_ids.append(record['objectID'])

    assert it.answer['nbPages'] == 3
    assert len(res_ids) == 5
    assert set(ro_index.ids) == set(res_ids)


def test_browse_from(ro_index):
    tmp = ro_index.browse(0, 4)
    it = ro_index.browse_from(cursor=tmp['cursor'])
    assert len(it['hits']) == 1


def test_search(ro_index):
    res = ro_index.search('')
    assert res['nbHits'] == 5

    res = ro_index.search('', {'hitsPerPage': 2})
    assert res['nbHits'] == 5
    assert res['hitsPerPage'] == 2

    res = ro_index.search('', {
        'attributesToRetrieve': ['name', 'email']
    })

    res_keys = res['hits'][0].keys()
    assert 'name' in res_keys
    assert 'email' in res_keys
    assert 'phone' not in res_keys
    assert 'city' not in res_keys
    assert 'country' not in res_keys

    res = ro_index.search('', {
        'attributesToRetrieve': 'name,email'
    })

    res_keys = res['hits'][0].keys()
    assert 'name' in res_keys
    assert 'email' in res_keys
    assert 'phone' not in res_keys
    assert 'city' not in res_keys
    assert 'country' not in res_keys

    res = ro_index.search('', {'analytics': False})
    assert res['nbHits'] == 5
    assert re.search(r'analytics=false', res['params'])

    res = ro_index.search(ro_index.data[2]['name'][0])
    assert res['nbHits'] >= 1
    res_ids = [elt['objectID'] for elt in res['hits']]
    assert ro_index.ids[2] in res_ids


def test_search_with_short_secured_api_key(ro_index):
    old_key = ro_index.client.api_key

    try:
        secured_api_key = ro_index.client.generate_secured_api_key(
            os.environ['ALGOLIA_API_KEY_SEARCH'],
            dict(filters=''),
        )
    except:
        raise RuntimeError("ALGOLIA_API_KEY_SEARCH must be set")

    assert len(secured_api_key) < MAX_API_KEY_LENGTH

    ro_index.client.api_key = secured_api_key
    res = ro_index.search('')
    assert res['nbHits'] == 5
    ro_index.client.api_key = old_key


def test_search_with_long_secured_api_key(ro_index):
    old_key = ro_index.client.api_key

    tags = set('x{0}'.format(100000 + i) for i in range(1000))
    try:
        secured_api_key = ro_index.client.generate_secured_api_key(
            os.environ['ALGOLIA_API_KEY_SEARCH'],
            dict(filters=' OR '.join(tags)),
        )
    except:
        raise RuntimeError("ALGOLIA_API_KEY_SEARCH must be set")

    assert len(secured_api_key) > MAX_API_KEY_LENGTH
    ro_index.client.api_key = secured_api_key
    res = ro_index.search('')
    assert res['nbHits'] == 0
    ro_index.client.api_key = old_key


def test_delete_object(rw_index):
    task = rw_index.delete_object(rw_index.ids[2])
    rw_index.wait_task(task['taskID'])

    params = {'attributesToRetrieve': ['objectID']}
    res_ids = [obj['objectID'] for obj in rw_index.browse_all(params)]
    assert len(res_ids) == 4
    assert rw_index.ids[2] not in res_ids
    for elt in res_ids:
        assert elt in rw_index.ids

def test_delete_objects(rw_index):
    task = rw_index.delete_objects(rw_index.ids[0:3])
    rw_index.wait_task(task['taskID'])

    params = {'attributesToRetrieve': ['objectID']}
    res_ids = [obj['objectID'] for obj in rw_index.browse_all(params)]
    assert len(res_ids) == 2
    for _ in range(3):
        assert rw_index.ids[0] not in res_ids
    for elt in res_ids:
        assert elt in rw_index.ids

def test_delete_by_query(rw_index):
    task = rw_index.delete_by_query(rw_index.data[2]['name'][0])
    rw_index.wait_task(task['taskID'])

    res = rw_index.search('', {'hitsPerPage': 0})
    assert res['nbHits'] < 5


def test_delete_by(index):
    obj1 = {'objectID': 'A', 'color': 'red'}
    obj2 = {'objectID': 'B', 'color': 'blue'}
    index.save_objects([obj1, obj2])
    task = index.set_settings({
        'attributesForFaceting': ['color']
    })
    index.wait_task(task['taskID'])

    task = index.delete_by({'filters': 'color:red'})
    print(task)
    index.wait_task(task['taskID'])

    res = index.search('')
    assert len(res['hits']) == 1
    del res['hits'][0]['_highlightResult']

    assert obj1 not in res['hits']
    assert obj2 in res['hits']


def test_batch(rw_index):
    factory = Factory()
    requests = [
        {
            'action': 'addObject',
            'body': factory.contacts()
        }, {
            'action': 'addObject',
            'body': factory.contacts()
        }
    ]

    task = rw_index.batch({'requests': requests})
    rw_index.wait_task(task['taskID'])
    res = rw_index.search('', {'hitsPerPage': 0})
    assert res['nbHits'] == 7

    body_update = dict(rw_index.data[2])
    body_update['name'] = 'Joseph Dia'
    requests = [
        {
            'action': 'updateObject',
            'body': body_update,
            'objectID': rw_index.ids[2]
        }, {
            'action': 'deleteObject',
            'objectID': rw_index.ids[0]
        }
    ]

    task = rw_index.batch(requests)
    rw_index.wait_task(task['taskID'])
    res = rw_index.get_object(rw_index.ids[2])
    del res['objectID']
    assert body_update == res

    try:
        rw_index.get_object(rw_index.ids[0])
        assert False
    except AlgoliaException as e:
        assert 'does not exist' in str(e)
