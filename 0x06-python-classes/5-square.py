#!/usr/bin/python3
""" defined class square"""


class Square:
    """ class square."""
    def __init__(self, size=0):
        """Private instance attribute: size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """ getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ returns the current square area. """
        return self.__size ** 2

    def my_print(self):
        """  prints in stdout the square with the char # """
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print('#' * self.size)
