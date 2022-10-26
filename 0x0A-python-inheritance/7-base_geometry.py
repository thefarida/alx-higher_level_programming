#!/usr/bin/python3
"""Defines an empty class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Not implemented."""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validates the value.

        Args:
            name (str): The name of the value.
            value (int): The value.
        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to zero.
        """
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
