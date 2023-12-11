#!/usr/bin/python3
# square.py
from models.rectangle import Rectangle
""" new class being defined """


class Square(Rectangle):
    """ class Square defined """

    def __init__(self, size, x=0, y=0, id=None):
        """ initialize the instance of class Square """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ get the size property of class square """
        return self.width

    @size.setter
    def size(self, value):
        """ set a new value for the property size """
        self.width = value
        self.height = value

    def __str__(self):
        """ Print the string representation of the class description """
        result = '[Square] ' + '(' + str(self.id) + ') '
        result += str(self.x) + '/' + str(self.y) + ' - '
        result += str(self.width)
        return result

    def update(self, *args, **kwargs):
        """
        Updates the values of the arguments of a class square
        The order of update is id, size, x, y
        If *args or **kwargs can be utilized to update the object
        """
        if args:
            arg_count = len(args)
            if arg_count >= 1:
                self.id = args[0]
            if arg_count >= 2:
                self.size = args[1]
            if arg_count >= 4:
                self.x = args[3]
            if arg_count >= 5:
                self.y = args[4]
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns the dictionary rep of class Rectangle """
        dict_t = {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
        return dict_t
