#!/usr/bin/python3
"""
Module 9-student
Represents student name and age.
"""


class Student():
    """Class represents student."""

    def __init__(self, first_name, last_name, age):
        """
        Initializes student.
        Args:
            first_name: first name of student.
            last_name: last name of student.
            age: age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns dictionary description with simple data structure
        (list, dictionary, dictionary, string)
        for JSON serialization of an object
        """
        return self.__dict__
