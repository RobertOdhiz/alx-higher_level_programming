#!/usr/bin/python3
""" Module with say_my_name function """


def say_my_name(first_name, last_name=""):
    """
    Print my name Function

    Args:
        first_name - First name
        last_name - Last Name

    Return:
        My name is <first name> <last name>
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
