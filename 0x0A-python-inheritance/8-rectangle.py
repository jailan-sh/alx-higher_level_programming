#!/usr/bin/python3
""" class BaseGeometry."""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    inhertance class Rectangle
    """
    def __init__(self, width, height):
        """ constractor for inhertance class Rectangle """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
