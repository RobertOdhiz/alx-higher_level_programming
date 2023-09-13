#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copy = {}
    for key, value in a_dictionary.items():
        copy[key] = value * 2

    return copy
