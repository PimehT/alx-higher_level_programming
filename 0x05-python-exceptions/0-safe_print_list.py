#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Description:
    Prints x elements of a list

    Parameters:
    my_list (List[int]): List to be printed. Default is empty list [].
    x (int): Number of elements to print, can be bigger than len of my_list
    Return: The real number of elements printed
    """
    i = 0
    while i < x:
        try:
            print("{}".format(my_list[i]), end="")
            i += 1
        except IndexError:
            break
    print()
    return i
