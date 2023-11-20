#!/usr/bin/python3
def safe_print_integer(value):
    """
    Description:
    Prints an integer with "{:d}".format().

    Parameters:
    value: integer to print

    Returns: True if value is integer and printed, otherwise False
    """
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
