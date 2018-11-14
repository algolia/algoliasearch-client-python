import pytest

from algoliasearch.account_client import AccountClient
from algoliasearch.helpers import AlgoliaException
from .helpers import rule_stub, synonym_stub


def test_copy_index_destination_must_not_exist(index, ro_index):
    response = index.save_object({'objectID': 'Foo', 'name': 'Bar'})
    index.wait_task(response['taskID'])

    response = ro_index.save_object({'objectID': 'Foo', 'name': 'Bar'})
    ro_index.wait_task(response['taskID'])

    with pytest.raises(AlgoliaException):
        AccountClient.copy_index(index, ro_index)


def test_copy_index_copy_the_index(index, ro_index):
    responses = [
        index.save_object({'objectID': 'Foo', 'name': 'Bar'}),
        index.batch_rules([rule_stub('foo')]),
        index.batch_synonyms([synonym_stub('foo')]),
        index.set_settings({'userData': 'foo'})
    ]

    for response in responses:
        index.wait_task(response['taskID'])

    response = ro_index.client.delete_index(ro_index.index_name)  # Make sure target don't exist.
    ro_index.wait_task(response['taskID'])

    responses = AccountClient.copy_index(index, ro_index)
    for response in responses:
        ro_index.wait_task(response['taskID'])

    # Assert objects got copied
    res = ro_index.search('')
    assert len(res['hits']) == 1
    del res['hits'][0]['_highlightResult']
    assert res['hits'][0] == {'objectID': 'Foo', 'name': 'Bar'}

    # Assert settings got copied
    settings = ro_index.get_settings()
    assert settings['userData'] == 'foo'

    # Assert synonyms got copied
    rule = ro_index.read_rule('foo')
    assert rule == rule_stub('foo')

    # Assert synonyms got copied
    synonym = ro_index.get_synonym('foo')
    assert synonym == synonym_stub('foo')
