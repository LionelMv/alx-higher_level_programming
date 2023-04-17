#!/usr/bin/python3
"""
Module contains class Base.
"""


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
