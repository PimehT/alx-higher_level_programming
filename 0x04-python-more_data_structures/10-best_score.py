#!/usr/bin/python3

def best_score(a_dictionary):
    """
    function returns a key with the biggest integer value
    """
    max_int = 0
    idx = ''
    if not a_dictionary:
        return
    for key, value in a_dictionary.items():
        if value > max_int:
            max_int = value
            idx = key
    return idx
