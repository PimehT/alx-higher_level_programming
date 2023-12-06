#!/usr/bin/python3
# 7-add_item.py
# Add an item to the list of items in a JSON file
import sys
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_items():
    """Adds an item to the list of items in a JSON file."""
    filename = "add_item.json"

    if path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, filename)

if __name__ == "__main__":
    add_items()
