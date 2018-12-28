def test_indexing(index, obj):
    obj_id = obj['objectID']
    task_id = index.save_object(obj)

    assert obj['name'] == index.get_object(obj_id)['name']
