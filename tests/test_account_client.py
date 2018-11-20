import pytest

from algoliasearch.account_client import AccountClient
from algoliasearch.helpers import AlgoliaException
from .helpers import rule_stub, synonym_stub
from .helpers import is_community

def test_copy_index_applications_must_be_different(client_1):

    index_1 = client_1.init_index('copy_index')
    index_2 = client_1.init_index('copy_index_2')

    with pytest.raises(AlgoliaException):
        AccountClient.copy_index(index_1, index_2)

def test_copy_index_copy_the_index_and_destination_must_not_exist(index_1, index_2):
    responses = [
        index_1.save_object({'objectID': 'one'}),
        index_1.batch_rules([rule_stub('one')]),
        index_1.batch_synonyms([synonym_stub('one')]),
        index_1.set_settings({'searchableAttributes': ['objectID']})
    ]

    for response in responses:
        index_1.wait_task(response['taskID'])

    responses = AccountClient.copy_index(index_1, index_2)
    for response in responses:
        index_2.wait_task(response['taskID'])

    # Assert objects got copied
    res = index_2.search('')
    assert len(res['hits']) == 1
    assert res['hits'][0] == {'objectID': 'one'}

    # Assert settings got copied
    settings = index_2.get_settings()
    assert settings['searchableAttributes'] == ['objectID']

    # Assert synonyms got copied
    rule = index_2.read_rule('one')
    assert rule == rule_stub('one')

    # Assert synonyms got copied
    synonym = index_2.get_synonym('one')
    assert synonym == synonym_stub('one')

    # Assert that copying again fails because index already exists
    with pytest.raises(AlgoliaException):
        AccountClient.copy_index(index_1, index_2)
