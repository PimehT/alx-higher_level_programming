#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    """
    Description:
    returns a list with all the values multiplied by a number
    without using loops

    Parameters:
    my_list: source list to which we multiply elements by a num
    number: number to multiply elements
    """
    return list(map(lambda x: x * number, my_list))
