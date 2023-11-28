#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    A function that prints "My name is <first name> <last name>
    Parameters:
    first_name: first name to print
    last_name: (optional) last name to print.
    If not provided it will be empty string ""

    Raise:
    TypeError if the names are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    return ("My name is {} {}".format(first_name, last_name))
