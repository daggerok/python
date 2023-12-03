from src.main.python.calc import add


def test_should_add_two_numbers():
    assert add(1, 2) == 3


def test_should_add_number_and_none():
    assert add(1, None) == 0


def test_should_add_none_and_number():
    assert add(None, 2) == 0
