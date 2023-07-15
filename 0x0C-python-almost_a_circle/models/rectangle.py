#!/usr/bin/python3
""" Model Rectangle that inherits from Base """

from models.base import Base


class Rectangle(Base):
    """ Class that defines a Rectangle model """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            msg = "width must be an integer"
            raise TypeError(msg)
        if value <= 0:
            msg = "width must be > 0"
            raise ValueError(msg)
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            msg = "height must be an integer"
            raise TypeError(msg)
        if value <= 0:
            msg = "height must be > 0"
            raise ValueError(msg)
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            msg = "x must be an integer"
            raise TypeError(msg)
        if value < 0:
            msg = "x must be >= 0"
            raise ValueError(msg)
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            msg = "y must be an integer"
            raise TypeError(msg)
        if value < 0:
            msg = "y must be >= 0"
            raise ValueError(msg)
        self.__y = value
