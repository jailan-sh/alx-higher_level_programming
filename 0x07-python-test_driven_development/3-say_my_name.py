#!/usr/bin/python3
"""

a function that prints My name

"""


def say_my_name(first_name, last_name=""):
    """
    a function that prints My name
    format : My name is <first name> <last name>
    args : first_name and last_name must be strings
    otherwise, raise a TypeError
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
