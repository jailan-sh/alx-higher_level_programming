#!/usr/bin/python3
"""

Integers addition

"""


def add_integer(a, b=98):
    """ function that adds 2 integers
    arg a and b : must be integers or floats
    otherwise TypeError is raised"""

    if isinstance(a, float):
        a = int(a)
    elif not isinstance(a, int):
        raise TypeError("a must be an integer")
    if isinstance(b, float):
        b = int(b)
    elif not isinstance(b, int):
        raise TypeError("b must be an integer")
    return (a + b)
