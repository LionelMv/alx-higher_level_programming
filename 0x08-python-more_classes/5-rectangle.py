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
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter
        Returns:
            width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter
        Raises:
            TypeError if width is not an integer
            ValueError if width is negative
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter
        Return:
            height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter
        Raises:
            TypeError if height is not an integer
            ValueError if height is negative
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the Rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """
        Returns the perimeter of the Rectangle.
        If width or height = 0, return 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """
        Returns a rectangle of #s.
        Returns an empty string if width or height = 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_hashes = "\n".join(["#" * self.__width
                                for rows in range(self.__height)])
        return rect_hashes

    def __repr__(self):
        "Returns the string representation of the Rectangle"
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ Deletes instance of class """
        print("Bye rectangle...")


# my_rectangle = Rectangle(2, 4)
# print("Area: {} - Perimeter: {}"
#       .format(my_rectangle.area(), my_rectangle.perimeter()))

# del my_rectangle

# try:
#     print(my_rectangle)
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))
