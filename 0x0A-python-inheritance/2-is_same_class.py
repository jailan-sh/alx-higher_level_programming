#!/usr/bin/python3
""" class MyList that inherits from list"""


def is_same_class(obj, a_class):
    """
    a function checks if object is exactly an instance of the specified class
    return true if object is exactly an instance of the specified class
    otherwise False
    """

    # return isinstance(obj, a_class) for class and subclasses
    return type(obj) == a_class  # exactly instance
