#!/usr/bin/python3
""" defining a class """


class Square:
    """ class square """

    def __init__(self, size=0):
        """
        initializing class square

        Args:
        size (int): size of square
        """
        self.__size = size

    @property
    def size(self):
        """ get square current size"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        set square size to new value

        Args:
        value (int): new size of square
        """
        if (not isinstance(value, int) or
                not isinstance(size, float)):
            raise TypeError("size must be an number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ return area of square """
        return (self.__size * self.__size)

    def __eq__(self, other):
        """ Define the == comparator """
        return self.area() == other.area()

    def __ne__(self, other):
        """ Define the != comparatot """
        return self.area() != other.area()

    def __lt__(self, other):
        """ Define the < comparator """
        return self.area() < other.area()

    def __le__(self, other):
        """ Define the <= comparator """
        return self.area() <= other.area()

    def __gt__(self, other):
        """ Define the > comparator """
        return self.area() > other.area()

    def __ge__(self, other):
        """ Define the >= compmarator """
        return self.area() >= other.area()
