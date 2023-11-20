#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """
    A function that prints an integer

    value: can be of any type

    Returns: True if value is integer, otherwise False and stderr message
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return False
