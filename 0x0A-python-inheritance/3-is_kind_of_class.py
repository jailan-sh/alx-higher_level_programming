#!/usr/bin/python3
""" class MyList that inherits from list"""


def is_kind_of_class(obj, a_class):
    """
    a function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from
    """
    return isinstance(obj, a_class)
