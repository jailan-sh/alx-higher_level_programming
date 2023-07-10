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

    def area(self):
        """ Public instance method """

        return self.__height * self.__width

    def __str__(self):
        """ Method for when print is used """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """ subclass Square """
    def __init__(self, size):
        """ constractor """
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ Public instance method calculate area"""
        return self.__size * self.__size
