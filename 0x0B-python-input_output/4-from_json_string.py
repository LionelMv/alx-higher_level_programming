#!/usr/bin/python3
"""
Module 4-from_json_string
Contains function that returns python object from JSON string
"""


def from_json_string(my_str):
    """Returns python obj from JSON string."""
    import json

    return json.loads(my_str)
