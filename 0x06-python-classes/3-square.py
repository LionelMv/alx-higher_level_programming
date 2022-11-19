#!/usr/bin/python3
"""
This module defines a square with private attribute size 
and public attribute area
"""


class Square:
    """Class represents a square"""

    def __init__(self, size=0):
        """
        Initilizes the class
        Args:
            size: size of a side of a square
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Calculates the  area of the square
        Returns: Area of the square
        """
        return self.__size ** 2
