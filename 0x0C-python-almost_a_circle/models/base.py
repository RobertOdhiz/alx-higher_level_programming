#!/usr/bin/python3
"""
Class Base - Will be the base of all classes in this project
"""


class Base:
    """ Representation of the base class """
    __nb_objects = 0
    def __init__(self, id=None):
        """ Initializing the class attributes """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
