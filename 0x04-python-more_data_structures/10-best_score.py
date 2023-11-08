#!/usr/bin/python3

def best_score(a_dictionary):
    """
    function returns a key with the biggest integer value
    """
    max_int = 0
    if not a_dictionary:
        return
    for value in a_dictionary.values():
        if value > max_int:
            max_int = value
    return max_int
