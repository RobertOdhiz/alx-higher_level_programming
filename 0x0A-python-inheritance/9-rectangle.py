#!/usr/bin/python3
"""
class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle Representation """
    def __init__(self, width, height):
        """ Initializing Rectangle """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Returns area of rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Magic method str returns string rep """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
