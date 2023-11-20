#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Description:
    Prints x elements of a list

    Parameters:
    my_list (List[int]): List to be printed. Default is empty list [].
    x (int): Number of elements from the beginning of the list that will be printed. Default is 0, which means all elements will be

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
