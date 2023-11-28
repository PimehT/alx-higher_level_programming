#!/usr/bin/python3
def print_square(size):
    """
    A function that prints a square with the character '#'

    Arg:
    size (int): size of the square
    """
    if ((isinstance(size, float) and size < 0) or
            not isinstance(size, int)):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif size == 0:
        return
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print("")
