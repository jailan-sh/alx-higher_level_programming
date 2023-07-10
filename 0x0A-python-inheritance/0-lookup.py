#!/usr/bin/python3
""" inheretance task """


def lookup(obj):
    """
    function that returns the list of available
    attributes and methods of an object
    args :
    obj : object to lookup
    Return : all attributes an methods of object
    """

    return dir(obj)
