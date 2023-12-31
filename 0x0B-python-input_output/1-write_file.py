#!/usr/bin/python3
""" Module with write_file function """


def write_file(filename="", text=""):
    """
    Representation of the function

    Args:
    filename- Name of file being written
    text - Text being written into the file

    Return:
    Number of bytes written into file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
