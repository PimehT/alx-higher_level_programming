#!/usr/bin/python3
# 100-append_after.py
""" inserts a line of text to a file at a certain point """


def append_after(filename="", search_string="", new_string=""):
    """
    insert line of text after certain string in file
    Args:
    filename (file): file to edit
    search_string (str): string to search for in file
    new_string (str): string to append to search_string
    """
    with open(filename, 'r+') as fp:
        lines = fp.readlines()
        fp.seek(0)
        for line in lines:
            fp.write(line)
            if search_string in line:
                fp.write(new_string)

        fp.truncate()
