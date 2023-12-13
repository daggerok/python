from pytest import mark
from recursive_prime_numbers import is_prime


@mark.parametrize(
    "number, expected",
    [
        (-1, False),
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (6, False),
        (7, True),
        (8, False),
    ]
)
def test_is_prime(number, expected):
    assert is_prime(number) == expected
