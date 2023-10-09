#!/usr/bin/python3
"""
Module with inherits_from function
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj inherits from a_class else False
    """
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
