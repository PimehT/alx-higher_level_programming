#!/usr/bin/python3
# 2-append_write.py
""" appends a text to the EOF and returns the number of chars """


def append_write(filename="", text=""):
    """
    a function that appends a string to the EOF
    Parameters:
    filename (str) : The name of the file you want to write in.
    If no value is provided, it will be set as "".
    text (str) : The content you want to add at the end of the file.
    If no value is provided, it will be set as "".
    Returns:
    Number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
