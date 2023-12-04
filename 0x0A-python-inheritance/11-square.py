#!/usr/bin/python3
# 11-square.py
""" defines a class Square that inherits from Rectangle """
Rectangle = __import__('9-rectangle').Rectangle
""" defining a new class """


class Square(Rectangle):
    """ class Square defined """

    def __init__(self, size):
        """ initialization of Square class """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        """ string representation of the class rectangle """
        result = "[" + self.__class__.__name__ + "] "
        result += str(self.__width) + "/" + str(self.__height)
        return result
