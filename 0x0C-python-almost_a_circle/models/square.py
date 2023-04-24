#!/usr/bin/python3
"""
Module contains class Square.
The class inherits from Rectangle class.
"""

from rectangle import Rectangle


class Square(Rectangle):
    """Class represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializing square attributes.
        Args:
            size: width and height of square.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Get size"""
        return self.width

    @size.setter
    def size(self, value):
        """Set size - sets width and height as size"""
        self.width = value
        self.height = value

    def __str__(self):
        """String representation of [Square] (<id>) <x>/<y> - <size>"""
        return (f"[Square] ({self.id}) "
                f"{self.x}/{self.y} - {self.size}")

    def update(self, *args, **kwargs):
        """
        If args: set attributes in this order: id, size, x, y.
        If no args given: set attributes according to kwargs.
        """
        if args:
            for k, v in enumerate(args):
                if k == 0:
                    self.id = v
                elif k == 1:
                    self.size = v
                elif k == 2:
                    self.x = v
                else:
                    self.y = v
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Return dictionary representation"""
        square_dict = {}
        square_dict["id"] = self.id
        square_dict["size"] = self.size
        square_dict["x"] = self.x
        square_dict["y"] = self.y
        return square_dict
