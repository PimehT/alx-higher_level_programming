#!/usr/bin/python3
# 6-load_from_json_file.py
""" creates an Object from a JSON file """
import json


def load_from_json_file(filename):
    """
    Loads a JSON file into a dictionary.
    Args:
    filename (str): The name of the file to be loaded.
    Returns:
    dict: A dictionary containing all data from the specified file.
    """
    with open(filename, 'r') as fp:
        return json.load(fp)
