#!/usr/bin/python3
""" Module that supplies the function print_square """


def print_square(size):
    """
    Function that prints a square of defined size

    args:
        size - Size of the square to be prnted
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
