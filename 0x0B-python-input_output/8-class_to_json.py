#!/usr/bin/python3
"""
Class to JSON
"""


def class_to_json(obj):
    """
    function that returns the dictionary description with simple data structure
    for JSON serialization of an object
    """
    mydic = {}
    if hasattr(obj, "__dict__"):
        mydic = obj.__dict__.copy()
    return mydic
