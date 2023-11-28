#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers/floats together and returns result in int
    Args:
    a (int or float): The first number to be added.
    b (int or float): The second number to be added. Default is 98

    Raises:
    TypeError: If the input parameters are not of type integer and not float
    """
    if (type(a) != int and type(a) != float):
        raise TypeError("a must be an integer")
    if (type(b) != int and type(b) != float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
