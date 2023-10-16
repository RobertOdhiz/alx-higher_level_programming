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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter for the x coordinate """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for the x coordinate """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter for the y coordinate """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for the y coordinate """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Finding area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ Prints in stdout the rectangle instance in # """
        for r in range(self.__y):
            print("")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        """ Method that assigns an argument to each attribute """
        arg_names = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i in range(len(args)):
                setattr(self, arg_names[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in arg_names:
                    setattr(self, key, value)

    def __str__(self):
        """ Returns the string representation of Rectangle """
        string = "[Rectangle] ({}) {}/{} - {}/{}".format(
                        self.id, self.__x, self.__y,
                        self.__width, self.__height)
        return string
