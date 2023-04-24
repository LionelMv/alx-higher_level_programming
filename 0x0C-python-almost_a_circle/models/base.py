#!/usr/bin/python3
"""
Module contains class Base.
"""
import json
import os


class Base:
    """
    Defines the Base class.
    Class attributes:
        __nb_objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the class.
        Args:
            id
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of list dict"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save json strings of all instances into file."""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            list_dicts = []
            if list_objs is not None:
                list_dicts = [cls.to_dictionary(obj) for obj in list_objs]
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns a list of JSON string representations."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        file_name = cls.__name__ + ".json"
        list_instances = []

        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                list_dicts = cls.from_json_string(f.read())
            list_instances = [cls.create(**d_ict) for d_ict in list_dicts]

        return list_instances
