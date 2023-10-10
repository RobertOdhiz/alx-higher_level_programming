#!/usr/bin/python3
""" Module with from_json_string """


import json


def from_json_string(my_str):
    """ Converts a json string to object """
    return json.loads(my_str)
