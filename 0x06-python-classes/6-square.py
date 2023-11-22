#!/usr/bin/python3
""" defining a class """


class Square:
    """ class square """

    def __init__(self, size=0, position=(0, 0)):
        """
        initializing class square

        Args:
        size (int): size of square
        position (tuple): position of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if (type(position) is not tuple or
                len(position) != 2 or
                not all(isinstance(i, int) for i in position) or
                any(i < 0 for i in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    @property
    def position(self):
        """ get square current position"""
        return self.__position

    @position.setter
    def position(self, value):
        """
        set square position to new value
        Args:
        value (tuple): new position of square
        """
        if (type(value) is not tuple or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                any(i < 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ return area of square """
        return (self.__size ** 2)

    def my_print(self):
        """ print square on basis of position """
        if self.__size == 0:
            print()
        else:
            [print() for i in range(self.__position[1])]
            for i in range(self.__size):
                [print(" ", end="") for j in range(self.__position[0])]
                [print("#", end="") for k in range(self.__size)]
                print()
