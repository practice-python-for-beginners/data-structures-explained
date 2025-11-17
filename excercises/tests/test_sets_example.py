from exercises.sets_example import create_set, add_to_set, find_union, find_intersection

def test_create_set_unique():
    s = create_set()
    assert len(s) == 4  # duplicates removed

def test_add_to_set():
    s = {1, 2}
    s = add_to_set(s, 3)
    assert 3 in s

def test_find_union():
    result = find_union({1, 2}, {2, 3})
    assert result == {1, 2, 3}

def test_find_intersection():
    result = find_intersection({1, 2, 3}, {2, 4})
    assert result == {2}
