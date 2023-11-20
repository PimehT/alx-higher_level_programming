#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
    A function that executes a function safely

    Parameters:
    1. fct: a pointer to a function

    Return:
    None if something happens during the function
    Prints stderr message preceded by 'Exception:'
    """
    try:
        return fct(*args)
    except (TypeError, ZeroDivisionError, ValueError, IndexError) as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return None
