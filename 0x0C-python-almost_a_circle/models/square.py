#!/usr/bin/python3
"""
Class Square that inherits from Rectangle
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """ Representation of a square """
    def __init__(self, size, x=0, y=0, id=None):
        """ Class Constructor """
        super().__init__(size, size, x, y, id)
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """ Returns formal representation of a string that describes Square """
        string = "[Square] ({}) {}/{} - {}".format(
                        self.id, self.x, self.y, self.width)
        return string
