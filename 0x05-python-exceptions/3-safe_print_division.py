#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Description:
    A function that divides 2 integers and prints the result

    Parameters:
    1. a (int): The dividend
    2. b (int): The divisor

    Returns the value fo the division, otherwise None
    """
    try:
        div = a / b
    except ZeroDivisionError:
        div = None
    finally:
        print("Inside result: {}".format(div))
        return div
