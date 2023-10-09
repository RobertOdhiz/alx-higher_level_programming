#!/usr/bin/python3
"""
class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """ Rectangle Representation """
    def __init__(self, size):
        """ Initializing Rectangle """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Returns area of rectangle """
        return self.__size * self.__size

    def __str__(self):
        """ Magic method str returns string rep """
        return "[Rectangle] {:d}/{:d}".format(self.__size, self.__size)
