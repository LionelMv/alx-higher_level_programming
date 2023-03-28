#!/usr/bin/python3
"""Define MagicClass"""
import math


class MagicClass:
    """Class represents a circle"""

    def __init__(self, radius):
        """
        Initilizes the class
        Args:
            radius: radius of the circle
            in
        Raises:
            TypeError: if radius is not an integer/float
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculates the area of the circle"""
        return math.pi * self.__radius ** 2

    def circumference(self):
        """Calculates the circumference of the circle"""
        return 2 * math.pi * self.__radius
