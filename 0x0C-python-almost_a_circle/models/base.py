#!/usr/bin/python3

""" base module"""

import json


class Base:
    """ class base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ consructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries:
            return "[]"
        else:
            data = json.dumps(list_dictionaries)
            return data

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        jlist = []
        if list_objs:
            for obj in list_objs:
                jlist.append(obj.to_dictionary())
        jstr = cls.to_json_string(jlist)
        file_name = cls.__name__ + ".json"
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(jstr)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances from a file """
        filename = cls.__name__ + ".json"

        try:
            with open(filename, encoding="utf-8") as myfile:
                rd = myfile.read()
                dicst = cls.from_json_string(rd)
                inslist = []
                for i in dicst:
                    inslist.append(cls.create(**i))
                return inslist
        except IOError:
            return []
