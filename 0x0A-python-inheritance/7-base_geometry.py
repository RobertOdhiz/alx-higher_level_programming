#!/usr/bin/python3
"""
Initializing class method BaseGeometry
"""


class BaseGeometry:
    """ Empty Class """
    def area(self):
        """ Undefined function area() """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates integer input """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
