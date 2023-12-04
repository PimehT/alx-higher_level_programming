#!/usr/bin/python3
# 3-is_kind_of_class.py
""" check if an object is an instance of a class directly or not """


def is_kind_of_class(obj, a_class):
    """
    A function that checks if an object is an instance of a class
    Parameters:
    obj (object) : The object to check
    a_class (type) : class to compare with
    Returns:
    bool : True if the object is an instance of,
        or if the object is an instance of a class that inherited from,
        the specified class
    False otherwise.
    """
    return isinstance(obj, a_class)
