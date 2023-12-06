#!/usr/bin/python3
# 0-read_file.py
""" reads a text file and prints it out to stdout """


def read_file(filename=""):
    """
    reads a text file and prints it out to stdout
    args:
    filename (str) : the name of the file you want to open.
    If no argument is provided, this function will return an empty string.
    """
    if not filename:
        print('')
    else:
        with open(filename, 'r', encoding="utf-8") as f:
            print("{}".format(f.read()))
