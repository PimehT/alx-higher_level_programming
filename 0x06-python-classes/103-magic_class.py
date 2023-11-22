#!/usr/bin/python3
""" defining a magic class based on a bytecode """

import math


class MagicClass:
    """ magic class defined """

    def __init__(self, radius=0):
        """
        magic class defined

        Args:
        radius (int): radius of a circle
        """
        self.__radius = 0
        if (type(radius) is not int and
                type(radius) is not float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ area of circle defined """
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """ circumferenct of circle defined """
        return (2 * math.pi * self.__radius)
