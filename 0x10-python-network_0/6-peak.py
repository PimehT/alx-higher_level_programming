#!/usr/bin/python3
""" function to find peak value"""


def find_peak(list_of_integers):
    """
    finds the peak value of a list of unsorted digits
    must be done with lowest complexity
    """
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    elif len(list_of_integers) == 2:
        return max(list_of_integers)

    mid = len(list_of_integers) // 2
    peak = list_of_integers[mid]
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return list_of_integers[mid]
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
