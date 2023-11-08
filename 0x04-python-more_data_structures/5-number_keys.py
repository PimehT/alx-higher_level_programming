#!/usr/bin/python3

def number_keys(a_dictionary):
    """
    Description:
    returns the number of keys in a dictionary

    Parameters:
    a_dictionary: dictionary to check

    Return:
    number of keys
    """
    count = 0
    for k in a_dictionary:
        count += 1
    return count
