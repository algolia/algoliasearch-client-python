from algoliasearch.user_insights_client import UserInsightsClient


def test_user_method(insights_client):
    assert isinstance(insights_client.user('userToken'), UserInsightsClient)


def test_send_event(insights_client, index_1):
    event = {
        'eventType': 'click',
        'eventName': 'foo',
        'index': index_1.index_name,
        'userToken': 'bar',
        'objectIDs': ['obj1', 'obj2']
    }

    response = insights_client.send_event(event)
    assert response['status'] == 200
    assert response['message'] == 'OK'


def test_send_events(insights_client, index_1):
    event = {
        'eventType': 'conversion',
        'eventName': 'foo',
        'index': index_1.index_name,
        'userToken': 'bar',
        'objectIDs': ['obj1', 'obj2']
    }

    response = insights_client.send_events([event])
    assert response['status'] == 200
    assert response['message'] == 'OK'
