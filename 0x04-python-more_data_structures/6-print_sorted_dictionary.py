#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
    print a sorted dictionary by ordered keys
    """
    sort_keys = sorted(a_dictionary)
    for i in sort_keys:
        print("{}: {}".format(i, a_dictionary[i]))
