#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """
    delete all values from the dictionary that are equal to 'value'
    return the modified dictionary
    """
    keys = [key for key, val in a_dictionary.items() if val == value]
    for key in keys:
        del a_dictionary[key]
    return a_dictionary
