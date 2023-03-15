#!/usr/bin/python3

# Cannot add or remove elements when iterating over a dictionary
def complex_delete(a_dictionary, value):
    for key in list(a_dictionary):
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
