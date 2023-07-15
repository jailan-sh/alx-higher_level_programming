#!/usr/bin/python3
""" class module """


class Student:
    """ class student """

    def __init__(self, first_name, last_name, age):
        """ constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance"""
        if not isinstance(attrs, list) or \
           not all(isinstance(i, str) for i in attrs):
            mydic = self.__dict__.copy()
        else:
            mydic = {i: self.__dict__[i] for i in attrs if i in self.__dict__}
        return mydic

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance """
        for i in json:
            self.__dict__[i] = json[i]
