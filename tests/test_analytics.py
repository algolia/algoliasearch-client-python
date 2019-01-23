from __future__ import print_function
from datetime import datetime

from algoliasearch.helpers import AlgoliaException


def test_ab_test_features(analytics, double_indexes):
    ab_test = {
        'name': "Python client ab integration test",
        'variants': [
            {'index': double_indexes[0].index_name, 'trafficPercentage': 90},
            {'index': double_indexes[1].index_name, 'trafficPercentage': 10},
        ],
        'endAt': datetime.utcnow().replace(day=29).strftime(
            "%Y-%m-%dT%H:%M:%SZ"),
    }
    response = analytics.add_ab_test(ab_test)
    analytics.wait_task(response['index'], response['taskID'])
    ab_test_id = response['abTestID']

    response = analytics.get_ab_test(ab_test_id)
    assert response['name'] == ab_test['name']

    response = analytics.get_ab_tests()
    assert len(response['abtests']) == response['count']
    assert response['total'] >= response['count']

    response = analytics.stop_ab_test(ab_test_id)
    analytics.wait_task(response['index'], response['taskID'])
    response = analytics.get_ab_test(ab_test_id)
    assert response['status'] == 'stopped'

    response = analytics.delete_ab_test(ab_test_id)
    analytics.wait_task(response['index'], response['taskID'])
    try:
        analytics.get_ab_test(ab_test_id)
        assert False
    except AlgoliaException as e:
        assert True


def test_aa_test_features(analytics, double_indexes):
    ab_test = {
        'name': "Python client aa integration test",
        'variants': [
            {'index': double_indexes[0].index_name, 'trafficPercentage': 90},
            {
                'index': double_indexes[0].index_name, 'trafficPercentage': 10,
                'customSearchParameters': {
                    'ignorePlurals': True
                }
            }
        ],
        'endAt': datetime.utcnow().replace(day=29).strftime(
            "%Y-%m-%dT%H:%M:%SZ"),
    }
    response = analytics.add_ab_test(ab_test)
    analytics.wait_task(response['index'], response['taskID'])
    ab_test_id = response['abTestID']

    response = analytics.get_ab_test(ab_test_id)
    assert response['name'] == ab_test['name']
    assert response['status'] == 'active'
