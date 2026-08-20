from app import add, subtract, greet


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 2) == 3


def test_greet():
    assert greet("Preethi") == "Hello, Preethi!"
