#!/usr/bin/python3
""" Module with load_from_json_file function """
import json


def load_from_json_file(filename):
    """ Function that loads a json file """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
