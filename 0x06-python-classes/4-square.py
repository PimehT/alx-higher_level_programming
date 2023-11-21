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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ return area of square """
        return (self.__size ** 2)
