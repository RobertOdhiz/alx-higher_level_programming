#!/usr/bin/python3
"""Definition of an empty rectangle class"""


class Rectangle:
    """
    Beginning of class definition
    """
    def __init__(self, width=0, height=0):
        """Initializing Rectangle vars"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for private instance att height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates Perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """Returns printable represantation of a rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
              string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string
