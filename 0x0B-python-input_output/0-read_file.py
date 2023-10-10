#!/usr/bin/python3
""" Module with read_file function """


def read_file(filename=""):
    """
    Representation of the function read_file

    Args: filename - Name of file being read
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                print(line, end='')
    except FileNotFoundError:
        pass
