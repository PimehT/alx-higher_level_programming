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

    def area(self):
        """ Calculate and return the area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Calculate and return the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ Return string representation of the object """
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            [print("#", end="") for j in range(self.__width)]
            if i != self.__height - 1:
                print()
        return ""
