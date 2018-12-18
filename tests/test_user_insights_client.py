def test_clicked_object_ids(insights_client, index_1):
    user_insights_client = insights_client.user('userToken')
    response = user_insights_client.clicked_object_ids('eventName', index_1.index_name, ['obj1', 'obj2'])
    assert response['status'] == 200
    assert response['message'] == 'OK'

def test_clicked_object_ids_after_search(insights_client, index_1):
    task = index_1.add_object({'objectID': 'obj1'}, 'obj1')
    index_1.wait_task(task['taskID'])

    query_id = index_1.search('query', {
        'clickAnalytics': True
    })['queryID']

    user_insights_client = insights_client.user('userToken')
    response = user_insights_client.clicked_object_ids_after_search('eventName', index_1.index_name, ['obj1', 'obj2'],
                                                         [1, 2], query_id)
    assert response['status'] == 200
    assert response['message'] == 'OK'


def test_clicked_filters(insights_client, index_1):
    user_insights_client = insights_client.user('userToken')
    response = user_insights_client.clicked_filters('eventName', index_1.index_name, ['filter:foo', 'filter:bar'])
    assert response['status'] == 200
    assert response['message'] == 'OK'

def test_converted_object_ids(insights_client, index_1):
    user_insights_client = insights_client.user('userToken')
    response = user_insights_client.converted_object_ids('eventName', index_1.index_name, ['obj1', 'obj2'])
    assert response['status'] == 200
    assert response['message'] == 'OK'

def test_converted_object_ids_after_search(insights_client, index_1):
    task = index_1.add_object({'objectID': 'obj1'}, 'obj1')
    index_1.wait_task(task['taskID'])

    query_id = index_1.search('query', {
        'clickAnalytics': True
    })['queryID']

    user_insights_client = insights_client.user('userToken')
    response = user_insights_client.converted_object_ids_after_search('eventName', index_1.index_name, ['obj1', 'obj2'],
                                                           query_id)
    assert response['status'] == 200
    assert response['message'] == 'OK'

def test_converted_filters(insights_client, index_1):
    user_insights_client = insights_client.user('userToken')
    response = user_insights_client.converted_filters('eventName', index_1.index_name, ['filter:foo', 'filter:bar'])
    assert response['status'] == 200
    assert response['message'] == 'OK'

def test_viewed_object_ids(insights_client, index_1):
    user_insights_client = insights_client.user('userToken')
    response = user_insights_client.viewed_object_ids('eventName', index_1.index_name, ['obj1', 'obj2'])
    assert response['status'] == 200
    assert response['message'] == 'OK'

def test_viewed_filters(insights_client, index_1):
    user_insights_client = insights_client.user('userToken')
    response = user_insights_client.viewed_filters('eventName', index_1.index_name, ['filter:foo', 'filter:bar'])
    assert response['status'] == 200
    assert response['message'] == 'OK'
