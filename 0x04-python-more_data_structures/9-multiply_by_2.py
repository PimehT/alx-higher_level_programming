#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
    Description:
    Returns a new dict with all its values multiplied by 2
    """
    new_dict = {key: value * 2 for key, value in a_dictionary.items()}
    return new_dict
