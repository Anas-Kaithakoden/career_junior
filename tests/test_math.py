def add(a, b):
    return a + b

def sub(a, b):
    return a - b


def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(2, 3) == -1
    assert sub(5, 3) == 2
    assert sub(0, 3) == 5


