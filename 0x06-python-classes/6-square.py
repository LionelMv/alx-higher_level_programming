#!/usr/bin/python3
"""
Module defines class Square with private size and position; and public area
Can access and update size and position
"""


class Square:
    """Class represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the class
        Args:
            size: size of a side of a square
            position: coordinates in the square.
        """

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """"
        Getter

        Return: size
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter

        Args:
            value: sets size to value if int and >= 0
        Raises:
            TypeError: if size != int
            ValueError: if size < 0
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """"
        Getter

        Return: position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter

        Args:
            value: sets position to tuple if value is tuple of 2 positive ints
        """

        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Calculates the  area of the square
        Returns: area
        """

        return self.__size ** 2

    def my_print(self):
        """Prints a square of hashes"""

        if self.__size == 0:
            print()

        print("\n" * self.__position[1], end="")
        print("\n".join([" " * self.__position[0] +
                        "#" * self.__size
                         for rows in range(self.__size)]))
