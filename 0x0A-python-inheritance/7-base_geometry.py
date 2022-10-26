#!/usr/bin/pyhton3
class BaseGeometry:
    """
    A class to implement geometrical shapes
    """

    def area(self):
        """
        Raises an exception when this function is called
        """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Checks an integer value

        Args:
            name (str): The name of the value.
            value (int): The value.

        Raises:
            TypeError: if 'value' isn't an integer.
            ValueError: If 'value' is less than or equal to zero.
        """

        if type(value) is not int:
            raise TypeError(name + ' must be an integer')

        if value <= 0:
            raise ValueError(name + ' must be greater than 0')
