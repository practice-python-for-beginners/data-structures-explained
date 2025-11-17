from exercises.dictionaries_example import create_dict, add_entry, remove_entry, get_value

def test_create_dict():
    d = create_dict()
    assert "name" in d and d["city"] == "Paris"

def test_add_entry():
    d = {"x": 1}
    d = add_entry(d, "y", 2)
    assert d["y"] == 2

def test_remove_entry():
    d = {"a": 1, "b": 2}
    d = remove_entry(d, "a")
    assert "a" not in d

def test_get_value():
    d = {"name": "Alice"}
    assert get_value(d, "name") == "Alice"
    assert get_value(d, "age") is None
