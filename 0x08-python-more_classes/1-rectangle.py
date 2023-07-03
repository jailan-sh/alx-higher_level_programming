#!/usr/bin/python3
""" define rectangle class """


class Rectangle:
    """ a class rectangle """
    def __init__(self, width=0, height=0):
        """ constructor of rectangle class
        Private instance attribute: width height """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """ to retrieve width """
        return self.__width

    @width.setter
    def width(self, value):
        """ method to set width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ method to set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
