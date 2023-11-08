#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Replace all occurrences of the 'search' with the 'replace' in a list.

    Parameters:
    my_list: initial list
    search (str): Element to replace in the list
    replace: The new element

    Return: list with changed elements or original list
    """
    result = []
    for item in my_list:
        if item == search:
            result.append(replace)
        else:
            result.append(item)
    return result
