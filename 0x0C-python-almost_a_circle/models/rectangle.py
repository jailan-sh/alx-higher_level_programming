#!/usr/bin/python3
""" rectangle module that inherited from Base """

from models.base import Base


class Rectangle(Base):
    """ class rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ ccalculate area """
        return self.height * self.width

    def display(self):
        """ prints in stdout the Rectangle with #"""
        if self.height == 0 or self.width == 0:
            return
        for i in range(self.y):
            print()
        for j in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """Print Method """
        st = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        st = st.format(self.id, self.x, self.y, self.width, self.height)
        return st

    def update(self, *args, **kwargs):
        """  assigns an argument to each attribute"""
        mylist = ["id", "width", "height", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    super().__init__(arg)
                elif i < len(mylist):
                    setattr(self, mylist[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ func. returns the dictionary representation of a Rectangle"""
        rdict = {"id": self.id, "width": self.width, "height": self.height,
                 "x": self.x, "y": self.y}
        return rdict
