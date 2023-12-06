#!/usr/bin/python3
# 3-to_json_string.py
""" returns the JSON representation of an object (string) """
import json


def to_json_string(my_obj):
    """
    a functions that returns the JSON representation of an object (string)
    Parameters:
    my_obj (object): The Python object you want to convert into a string.
    """
    return json.dumps(my_obj)
