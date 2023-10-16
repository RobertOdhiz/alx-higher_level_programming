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
        """ Public getter for size attribute """
        return self.width

    @size.setter
    def size(self, value):
        """ Public Setter for size prop """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Assigns attributes """
        list_args = ['id', 'size', 'x', 'y']
        if args:
            for arg in range(len(args)):
                setattr(self, list_args[arg], args[arg])
        else:
            for key, value in kwargs.items():
                if key in list_args:
                    setattr(self, key, value)

    def __str__(self):
        """ Returns formal representation of a string that describes Square """
        string = "[Square] ({}) {}/{} - {}".format(
                        self.id, self.x, self.y, self.width)
        return string

    def to_dictionary(self):
        """ Returns Dictionary representation of Square """
        return {
                'id': self.id,
                'x': self.x,
                'size': self.width,
                'y': self.y
        }
