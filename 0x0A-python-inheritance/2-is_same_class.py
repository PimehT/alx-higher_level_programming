#!/usr/bin/python3
# 2-is_same_class.py
""" check if an object is specifically a certain type """


def is_same_class(obj, a_class):
    """
    Function that returns True if the object is exactly an instance
    of the specified class
    Parameters:
    obj (object) : The object to check
    a_class (type) : The class to compare with
    Returns:
    bool : True if the object is exactly an instance of the class,
    False otherwise
    """
    return (type(obj) == a_class)
