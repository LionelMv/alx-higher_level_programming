#!/usr/bin/python3
"""
This module defines a function `add_attribute`.
"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj: The object to which the attribute is added.
        attribute: The attribute to be added.
        value: The value of the attribute.

    Raises:
        TypeError: If the object can't have a new attribute.
    """
    # Check if the object has the __dict__ attribute and it's writable
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    # Set the attribute in the object's dictionary
    obj.__dict__[attribute] = value
