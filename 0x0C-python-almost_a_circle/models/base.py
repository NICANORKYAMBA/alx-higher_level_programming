#!/usr/bin/python3
"""Defines a base model class."""
import json
from os import path


class Base:
    """Represent the base model.

    Represents the "base" for all other classes in project 0x0C*.

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns a json string representation of list of dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""

        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """returns a list of JSON string representation

        Args:
            json_string ([str]): [represents list of dictionaries]
        """
        if json_string is None or json_string == '[]':
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """return a class instantied from a dictionary of attributes.

        Args:
            **dictionary [dict]: Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == 'Rectangle':
                newclass = cls(1, 1)
            else:
                newclass = cls(1)
        newclass.update(**dictionary)
        return newclass

    @classmethod
    def load_from_file(cls):
        """return a list of classes instantiated from a file of JSON strings.

        reads from `<cls.__name__>.json`.

        returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        if path.exists(filename) is True:
            with open(filename, "r", encoding="utf-8") as f:
                list_objects = Base.from_json_string(f.read())
                return [cls.create(**dicts) for dicts in list_objects]
        else:
            return []
