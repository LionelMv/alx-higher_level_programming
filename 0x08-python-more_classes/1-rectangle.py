#!/usr/bin/python3
"""
Module defines a rectangle
"""


class Rectangle:
    """
    Class represents a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle (default: 0).
            height (int): The height of the rectangle (default: 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: if the value is not an integer.
            ValueError: if the value is negative.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is negative
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

# my_rectangle = Rectangle(2, 4)
# print(my_rectangle.__dict__)

# my_rectangle.width = 10
# my_rectangle.height = 3
# print(my_rectangle.__dict__)
