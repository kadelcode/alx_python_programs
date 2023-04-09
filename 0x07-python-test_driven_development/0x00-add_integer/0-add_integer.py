#!/usr/bin/python3
"""Addition function"""


def add_integer(a, b=98):
    """A function that adds two integers"""

    if type(a) == float:
        a = int(a)

    if not isinstance(a, int):
        raise TypeError('a must be an integer')

    if type(b) == float:
        b = int(b)

    if not isinstance(b, int):
        raise TypeError('b must be an integer')

    return (a + b)
