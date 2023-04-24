#!/usr/bin/python3
"""
Module contains class Rectangle.
The class inherits from Base class.
"""


from models.base import Base


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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @property
    def x(self):
        """Gets x"""
        return self.__x

    @property
    def y(self):
        """Gets y"""
        return self.__y

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Sets x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Sets y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

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
        """
        String representation of
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return (f"[Rectangle] ({self.id}) "
                f"{self.__x}/{self.__y} - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """
        If args: set attributes in this order: id, width, height, x, y
        If no args given: set attributes according to kwargs
        """
        if args:
            for k, v in enumerate(args):
                if k == 0:
                    self.id = args[0]
                elif k == 1:
                    self.__width = args[1]
                elif k == 2:
                    self.__height = args[2]
                elif k == 3:
                    self.__x = args[3]
                else:
                    self.__y = args[4]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.__width = kwargs["width"]
            if "height" in kwargs:
                self.__height = kwargs["height"]
            if "x" in kwargs:
                self.__x = kwargs["x"]
            if "y" in kwargs:
                self.__y = kwargs["y"]

    def to_dictionary(self):
        """Return dictionary representation of the rectangle."""
        rect_dict = {}
        rect_dict["id"] = self.id
        rect_dict["width"] = self.width
        rect_dict["height"] = self.height
        rect_dict["x"] = self.x
        rect_dict["y"] = self.y
        return rect_dict
