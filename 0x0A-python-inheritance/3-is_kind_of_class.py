#!/usr/bin/python3
"""
Module with function that check instance is_kind_class
"""


def is_kind_of_class(obj, a_class):
    """
    Returns: True if obj is an instance or instance of class
    inherited from a_class otherwise false
    """
    return isinstance(obj, a_class)
