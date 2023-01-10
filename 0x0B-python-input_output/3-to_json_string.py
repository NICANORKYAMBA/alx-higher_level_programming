#!/usr/bin/python3
import json
"""module that returns the JSON representation
of an object (string)"""


def to_json_string(my_obj):
    """returns JSON rep of my_obj"""
    return json.dumps(my_obj)
