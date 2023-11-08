#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    returns a set that contains element only present in one of the sets

    Parameters:
    set_1: first set to check
    set_2: second set to check

    Return:
    new set with unique elements
    """
    return set_1 ^ set_2
