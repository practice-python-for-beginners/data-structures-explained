from exercises.lists_example import create_list, append_to_list, remove_from_list, sort_list

def test_create_list():
    assert create_list() == [1, 2, 3, 4, 5]

def test_append_to_list():
    assert append_to_list([1, 2], 3) == [1, 2, 3]

def test_remove_from_list():
    assert remove_from_list([1, 2, 3], 2) == [1, 3]

def test_sort_list():
    assert sort_list([3, 1, 2]) == [1, 2, 3]
