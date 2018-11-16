import pytest

from algoliasearch.account_client import AccountClient
from algoliasearch.helpers import AlgoliaException
from .helpers import rule_stub, synonym_stub
from .helpers import is_community

def test_copy_index_applications_must_be_different(index, ro_index):
    response = index.save_object({'objectID': 'Foo', 'name': 'Bar'})
    index.wait_task(response['taskID'])

    response = ro_index.save_object({'objectID': 'Foo', 'name': 'Bar'})
    ro_index.wait_task(response['taskID'])

    with pytest.raises(AlgoliaException):
        AccountClient.copy_index(index, ro_index)


@pytest.mark.skipif(is_community,
                    reason='Cross application methods cannot be tested by the community')
def test_copy_index_destination_must_not_exist(index, mcm_index):
    response = index.save_object({'objectID': 'Foo', 'name': 'Bar'})
    index.wait_task(response['taskID'])

    response = mcm_index.save_object({'objectID': 'Foo', 'name': 'Bar'})
    mcm_index.wait_task(response['taskID'])

    with pytest.raises(AlgoliaException):
        AccountClient.copy_index(index, mcm_index)


@pytest.mark.skipif(is_community,
                    reason='Cross application methods cannot be tested by the community')
def test_copy_index_copy_the_index(index, mcm_index):
    responses = [
        index.save_object({'objectID': 'Foo', 'name': 'Bar'}),
        index.batch_rules([rule_stub('foo')]),
        index.batch_synonyms([synonym_stub('foo')]),
        index.set_settings({'userData': 'foo'})
    ]

    for response in responses:
        index.wait_task(response['taskID'])

    response = mcm_index.client.delete_index(mcm_index.index_name)  # Make sure target don't exist.
    mcm_index.wait_task(response['taskID'])

    responses = AccountClient.copy_index(index, mcm_index)
    for response in responses:
        mcm_index.wait_task(response['taskID'])

    # Assert objects got copied
    res = mcm_index.search('')
    assert len(res['hits']) == 1
    del res['hits'][0]['_highlightResult']
    assert res['hits'][0] == {'objectID': 'Foo', 'name': 'Bar'}

    # Assert settings got copied
    settings = mcm_index.get_settings()
    assert settings['userData'] == 'foo'

    # Assert synonyms got copied
    rule = mcm_index.read_rule('foo')
    assert rule == rule_stub('foo')

    # Assert synonyms got copied
    synonym = mcm_index.get_synonym('foo')
    assert synonym == synonym_stub('foo')
