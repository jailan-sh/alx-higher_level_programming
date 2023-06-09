#!/usr/bin/python3
""" class BaseGeometry."""


class BaseGeometry:
    """
    a class BaseGeometry
    """

    def area(self):
        """ Public instance method that raises an Exception with the message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method validate value
        args: name is always a string
        value integer > 0
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
