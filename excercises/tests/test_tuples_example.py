from exercises.tuples_example import create_tuple, access_tuple, unpack_tuple

def test_create_tuple():
    tpl = create_tuple()
    assert isinstance(tpl, tuple)
    assert tpl[0] == "Python"

def test_access_tuple():
    tpl = create_tuple()
    assert access_tuple(tpl, 1) == 3.11

def test_unpack_tuple():
    tpl = create_tuple()
    msg = unpack_tuple(tpl)
    assert "Python" in msg and "Beginner" in msg
