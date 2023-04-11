#!/usr/bin/python3
"""
Module 3-is_kind_of_class
Checks if object is an instance of a class or an inherited class.
"""


def is_kind_of_class(obj, a_class):
    """
    Return:
        True if object is an instance of a class or an inherited class.
    """
    return isinstance(obj, a_class)
