#!/usr/bin/python3
""" defining a new class """


class BaseGeometry:
    """ class BaseGeometry defined """

    def area(self):
        """ raise error message for calling area without parameters """
        raise Exception("area() is not implemented")
