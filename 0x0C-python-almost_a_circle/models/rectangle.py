#!/usr/bin/python3
"""
Class Rectangle - Inherits from Base
"""
from .base import Base


class Rectangle(Base):
    """ Representation of the base class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Instatiating class attributes """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter for the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width """
        self.__width = value

    @property
    def height(self):
        """ Getter for the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height """
        self.__height = value

    @property
    def x(self):
        """ Getter for the x coordinate """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for the x coordinate """
        self.__x = value

    @property
    def y(self):
        """ Getter for the y coordinate """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for the y coordinate """
        self.__y = value
