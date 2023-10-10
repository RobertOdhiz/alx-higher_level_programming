#!/usr/bin/python3
""" Module with append_write function """


def append_write(filename="", text=""):
    """
    Representation of the function

    Args:
    filename- Name of file being written
    text - Text being written into the file

    Return:
    Number of bytes written into file
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
