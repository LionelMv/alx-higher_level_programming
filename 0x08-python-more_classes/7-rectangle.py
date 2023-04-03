#!/usr/bin/python3
"""
Module defines a rectangle
"""


class Rectangle:
    """
    Class represents a rectangle.

    Args:
        number_of_instances (int): The number of Rectangle instances created.
        print_symbol (any type): The symbol used to represent a rectangle
            in string form.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle (default: 0).
            height (int): The height of the rectangle (default: 0).
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

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

    def area(self):
        """Returns the area of the Rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Returns the string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_hashes = "\n".join([str(self.print_symbol) * self.__width
                                for rows in range(self.__height)])
        return rect_hashes

    def __repr__(self):
        """Returns the string representation of the rectangle instance."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Deletes an instance of a Rectangle."""
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1


# my_rectangle_1 = Rectangle(8, 4)
# print(my_rectangle_1)
# print("--")
# my_rectangle_1.print_symbol = "&"
# print(my_rectangle_1)
# print(my_rectangle_1.__dict__)
# print("--")

# my_rectangle_2 = Rectangle(2, 1)
# print(my_rectangle_2)
# print("--")
# Rectangle.print_symbol = "C"
# print(my_rectangle_2)
# print("--")

# my_rectangle_3 = Rectangle(7, 3)
# print(my_rectangle_3)

# print("--")

# my_rectangle_3.print_symbol = ["C", "is", "fun!"]
# print(my_rectangle_3)

# print("--")
