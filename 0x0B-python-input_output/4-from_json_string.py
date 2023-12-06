#!/usr/bin/python3
# 4-from_json_string.py
""" returns an object (Python data struture) represented by JSON """
import json


def from_json_string(my_str):
    """
    a function that returns an object (Python data structure)
    represented by a JSON string
    Args:
    my_str : str, the input JSON string to be parsed.
    """
    return json.loads(my_str)
