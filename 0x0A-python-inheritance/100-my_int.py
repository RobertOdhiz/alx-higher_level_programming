#!/usr/bin/python3
"""
Beginning of class MyInt that inherits from
int
"""


class MyInt(int):
    """ Representing the Class """
    def __eq__(self, other):
        """ Overriding the == """
        return super().__ne__(other)

    def __ne__(self, other):
        """ Overriding the != """
        return super().__eq__(other)
