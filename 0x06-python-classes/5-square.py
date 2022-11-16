#!/usr/bin/python3
"""This module defines a square"""


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

    @property
    def size(self):
        """Retrieves size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the new size of the square"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates the  area of the square
        Returns: Area of the square
        """

        return self.__size ** 2

    def my_print(self):
        """Prints a square of hashes"""

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
