#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Description:
    Prints the first x integers from a list

    Parameters:
    my_list (List): List that may contain any type of values.
    x (int): Number of elements from the beginning of the list to be printed.

    Return: The real number of integers printed
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (TypeError, ValueError):
            continue
    print()
    return count
