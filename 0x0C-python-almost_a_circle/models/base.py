#!/usr/bin/python3
# base.py
""" contains class Base which is the basis for other class """
import json
""" Defining a new class """


class Base:
    """ Base class defined """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialization of class
        Arg:
        id (int): id of initialization
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        Arg:
        json_string (str): is a string representation of a list of dicts
        """
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        filename = cls.__name__ + ".json"

        if list_objs is None:
            list_objs = []

        with open(filename, 'w', encoding="utf-8") as fp:
            j = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            return fp.write(j)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        dummy_init = cls(1, 1)
        dummy_init.update(**dictionary)
        return dummy_init

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as fp:
                data = fp.read()
                if not data:
                    return []
                else:
                    json_data = cls.from_json_string(data)
                    return [cls.create(**elem) for elem in json_data]
        except FileNotFoundError:
            return []
