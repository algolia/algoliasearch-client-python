from __future__ import unicode_literals
import os
import time
from algoliasearch.helpers import PY2

STR_TYPE = unicode if PY2 else str


def uniq_user_id():
    name = 'python-client'
    if 'TRAVIS' not in os.environ:
        return name
    job = os.environ['TRAVIS_JOB_NUMBER']
    return '{}-travis={}'.format(name, job)


def test_1_list_clusters(mcm_client):
    answer = mcm_client.list_clusters()

    assert isinstance(answer, dict)
    assert isinstance(answer['clusters'], list)
    assert answer['clusters']
    assert isinstance(answer['clusters'][0]['clusterName'], STR_TYPE)
    assert isinstance(answer['clusters'][0]['nbRecords'], int)
    assert isinstance(answer['clusters'][0]['nbUserIDs'], int)
    assert isinstance(answer['clusters'][0]['dataSize'], int)


def test_2_assign_user_id(mcm_client):
    name = mcm_client.list_clusters()['clusters'][0]['clusterName']
    answer = mcm_client.assign_user_id(uniq_user_id(), name)

    assert isinstance(answer, dict)
    assert isinstance(answer['createdAt'], STR_TYPE)

    time.sleep(2) # Sleep to let the cluster publish the change


def test_3_list_user_ids(mcm_client):
    answer = mcm_client.list_user_ids()

    assert isinstance(answer, dict)
    assert isinstance(answer['userIDs'], list)
    assert answer['userIDs']
    assert isinstance(answer['userIDs'][0]['userID'], STR_TYPE)
    assert isinstance(answer['userIDs'][0]['clusterName'], STR_TYPE)
    assert isinstance(answer['userIDs'][0]['nbRecords'], int)
    assert isinstance(answer['userIDs'][0]['dataSize'], int)


def test_4_get_top_user_id(mcm_client):
    cluster_name = mcm_client.list_clusters()['clusters'][0]['clusterName']
    answer = mcm_client.get_top_user_id()

    assert isinstance(answer, dict)
    assert isinstance(answer['topUsers'], dict)
    assert answer['topUsers']
    assert isinstance(answer['topUsers'][cluster_name], list)
    assert isinstance(answer['topUsers'][cluster_name][0]['userID'], STR_TYPE)
    assert isinstance(answer['topUsers'][cluster_name][0]['nbRecords'], int)
    assert isinstance(answer['topUsers'][cluster_name][0]['dataSize'], int)

def test_5_get_user_id(mcm_client):
    answer = mcm_client.get_user_id(uniq_user_id())

    assert isinstance(answer, dict)
    assert isinstance(answer['userID'], STR_TYPE)
    assert isinstance(answer['clusterName'], STR_TYPE)
    assert isinstance(answer['nbRecords'], int)
    assert isinstance(answer['dataSize'], int)

def test_6_search_user_ids(mcm_client):
    clusterName = mcm_client.list_clusters()['clusters'][0]['clusterName']
    answer = mcm_client.search_user_ids(uniq_user_id(), clusterName, 0, 1000)


    assert isinstance(answer, dict)
    assert isinstance(answer['nbHits'], int)
    assert isinstance(answer['page'], int)
    assert isinstance(answer['hitsPerPage'], int)
    assert isinstance(answer['hits'], list)
    assert answer['hits']
    assert isinstance(answer['hits'][0]['userID'], STR_TYPE)
    assert isinstance(answer['hits'][0]['clusterName'], STR_TYPE)
    assert isinstance(answer['hits'][0]['nbRecords'], int)
    assert isinstance(answer['hits'][0]['dataSize'], int)

def test_7_remove_user_id(mcm_client):
    answer = mcm_client.remove_user_id(uniq_user_id())

    print(answer)
    assert isinstance(answer, dict)
    assert isinstance(answer['deletedAt'], STR_TYPE)
