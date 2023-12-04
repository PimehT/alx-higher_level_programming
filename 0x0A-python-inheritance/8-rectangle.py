#!/usr/bin/python3
# 8-rectangle.py
""" contains a class that has inherited attributes of BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry

""" Defining a new class """


class Rectangle(BaseGeometry):
    """ class Rectangle with parent class BaseGeometry """

    def __init__(self, width, height):
        """
        Initialize new Rectangle
        Parameters:
        - width (int) : Width of the rectangle.
        - height (int) : Height of the rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
