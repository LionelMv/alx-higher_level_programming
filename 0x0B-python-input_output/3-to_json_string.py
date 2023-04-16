#!/usr/bin/python3
"""
Module 3-to_json_string
Contains function that returns JSON representation of obj (string)
"""


def to_json_string(my_obj):
    """Returns JSON string representation of obj"""
    import json

    return json.dumps(my_obj)
