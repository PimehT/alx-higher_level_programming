#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    if not my_list:
        return None
    max_n = 0
    for i in my_list:
        if i > max_n:
            max_n = i
    return max_n
