#!/usr/bin/python3
""" Module with to_json_string """


import json


def to_json_string(my_obj):
    """ Converts an object to json """
    return json.dumps(my_obj)
