import time



def test_indexing(index, obj):
    obj_id = obj['objectID']
    index.save_object(obj)

    time.sleep(3)

    assert obj['name'] == index.get_object(obj_id)['name']
