#!/usr/bin/python3
""" defining a new class """


class BaseGeometry:
    """ class BaseGeometry defined """

    def area(self):
        """ raise error message for calling area without parameters """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        check if the given parameter is an integer or not
        Parameters:
        - name (str) : name of the parameter
        - value (int) : value to be checked
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
