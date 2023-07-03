#!/usr/bin/python3
""" define rectangle class """


class Rectangle:
    """ a class rectangle """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ constructor of rectangle class
        Private instance attribute: width height """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ method to get area """
        return self.height * self.width

    def perimeter(self):
        """ method to get primeter """
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return ((self.width + self.height) * 2)

    def __str__(self):
        """ print rectangle to stdout # """
        if self.height == 0 or self.width == 0:
            return ""
        else:
            rec_str = ""
            for i in range(self.height):
                for j in range(self.width):
                    rec_str += '#'
                if (i != (self.height - 1)):
                    rec_str += '\n'
        return rec_str

    def __repr__(self):
        """represent a string may used to create new object from class"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """ del instance from class """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
