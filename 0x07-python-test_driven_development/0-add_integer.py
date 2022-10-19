#!/usr/bin/pythton3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Add two numbers a and b.

    Return the addition of the numbers.Float arguments
    are to be typecasted to integers before addition.

    Raises:
        TypeError: If a or b is a non-integer and a non-float.
    """
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')

    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return (int(a) + int(b))
