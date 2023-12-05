#!/usr/bin/python3
# 101-add_attribute.py
""" this module adds attribute to be added if allowed """

def add_attribute(obj, attr, value):
    """
    adds an new attribute to an object if it is possible
    Args:
    obj : the object that will have its attributes modified
    attr: the name of the attribute being added
    value: the value of the attribute being added
    Raises:
    TypeError: if attribute cannot be added
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
