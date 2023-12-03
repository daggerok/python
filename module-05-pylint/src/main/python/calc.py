"""
Module documentation
"""


def add(x, y):
    """
    Addition function
    :param x: 1st operand
    :param y: 2nd operand
    :return: sum if both :x and :y are not None or zero
    """
    return x + y if x is not None and y is not None else 0
