#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Description:
    updates value of key or creates key-value pair if it doesnt exist

    Parameters:
    a_dictionary: dictionary to modify
    key: key to update or create
    value: value to create or replace existing one
    """
    if key in a_dictionary:
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value
    return a_dictionary
