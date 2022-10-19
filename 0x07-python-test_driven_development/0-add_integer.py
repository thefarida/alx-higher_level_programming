#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Return integer addition of a and b.

    Floats are typecasted to integers before addition.

    Raise:
        TypeError: If a or b are not integers.
    """
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')

    if type(b) not in (int, float):
        raise TypeError('b must be an integer')

    return a + b
