#!/usr/bin/python3
# 1-write_file.py
""" writes a string into a UTF8 file and returns the number of chars """
def write_file(filename="", text=""):
    """
    a function that writes a string to a text file
    Args:
    - filename (str, optional): the name of the file. Defaults to "".
    - text (str, optional): the content you want to write in the file.
    Defaults to "".
    Returns:
    the number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
