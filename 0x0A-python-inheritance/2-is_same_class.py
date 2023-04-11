#!/usr/bin/python3
"""
Module 2-is_same_class
Returns True if object is exactly an instance of specified class.
"""


def is_same_class(obj, a_class):
    """
    Return:
        True if object is an instance of the class, otherwise return false
    """
    return type(obj) == a_class
