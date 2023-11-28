#!/usr/bin/python3
""" defining a new class """


class LockedClass:
    """
    Locked class defined
    It prevents user from creating new instance
    if the attribute is not called <first_name>
    """

    __slots__ = ["first_name"]
