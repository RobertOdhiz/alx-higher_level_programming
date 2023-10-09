#!/usr/bin/python3
"""
Contains function that checks if the objects are exactly same
"""


def is_same_class(obj, a_class):
    """
    Function definition
    Args: obj - object checked, a_class - class instance
    """
    return (type(obj) == a_class)
