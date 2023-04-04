#!/usr/bin/python3
"""
Defines class with no class or object attribute
Control dynamically created instance attributes
"""


class LockedClass:
    """
    Prevents user from creating new instance attribute dynamically
    unless attribute is first_name
    """

    __slots__ = "first_name"

    def __init__(self, first):
        """
        Initializes the class to only instantiate first_name

        Args:
        first_name (str)
        """
        self.first_name = first
