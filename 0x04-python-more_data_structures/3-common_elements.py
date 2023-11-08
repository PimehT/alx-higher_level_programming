#!/usr/bin/python3

def common_elements(set_1, set_2):
    """
    Returns the set containing the common elements in both sets

    Parameters:
    set_1: first set to compare
    set_2: second set to compare

    Returns: set with common elements
    """
    if not set_1:
        return
    if not set_2:
        return
    new_set = []
    for item in set_1:
        if item in set_2:
            new_set.append(item)
    return new_set
