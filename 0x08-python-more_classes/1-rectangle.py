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
        Initializing the class.
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        getter
        Returns:
            width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter
        Raises error if width is not int or >= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        getter
        Return:
            height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter
        Raises error if height is not int or >= 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
