#!/usr/bin/python3
# 5-save_to_json_file.py
""" writes an Object to a text file using JSON rep """
import json


def save_to_json_file(my_obj, filename):
    """
    a function that writes an Object to a text file,
    using a JSON representation
    Args:
    my_obj (object): the object you want to write to a file.
    This can be any Python object such as list, dict or custom class objects.
    filename (str): The name of the output file.
    """
    with open(filename, 'w', encoding="utf-8") as my_fp:
        return json.dump(my_obj, my_fp)
