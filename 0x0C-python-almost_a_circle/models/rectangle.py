#!/usr/bin/python3
"""
Module contains class Rectangle.
The class inherits from Base class.
"""


from base import Base


class Rectangle(Base):
    """This class represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the rectangle instance.
        Args:
            width: width of the rectangle.
            height: height of the rectangle.
            x:
            y:

        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets x"""
        return self.x

    @x.setter
    def x(self, value):
        """Sets x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.x = value

    @property
    def y(self):
        """Gets y"""
        return self.y

    @y.setter
    def y(self, value):
        """Sets y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.y = value

    def area(self):
        """Returns area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Print to stdout a rectangle using #'s"""
        for j in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Prints [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return (f"[Rectangle] ({self.id}) "
                f"{self.__x}/{self.__y} - {self.__width}/{self.__height}")
