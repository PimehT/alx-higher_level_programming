#!/usr/bin/python3
""" defining a new class """


class Rectangle:
    """ Rectangle class defined """

    def __init__(self, width=0, height=0):
        """
        Initialize the object of class Rectangle
        Args:
        width (int): width of the rectangle
        height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ get width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width to a new value
        Args:
        value (int): new width for the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ get height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height to a new value
        Args:
        value (int): new height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
