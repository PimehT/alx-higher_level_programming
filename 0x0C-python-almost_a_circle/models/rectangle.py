#!/usr/bin/python3
# rectangle.py
""" cotains the class Rectangle which inherits features from Base """
from models.base import Base


class Rectangle(Base):
    """ class Rectangle defined """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize the class square
        Args:
        width (int): width of shape
        height (int): height of shape
        x (int): x coordinate of shape
        y (int): y coordinate of shape
        id (int): id of the shape created
        """
        super().__init__(id)

        init_t = {'width': width, 'height': height, 'x': x, 'y': y}
        for key, value in init_t.items():
            self.integer_validator(key, value)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def integer_validator(self, name, value):
        """
        check if the given parameter is an integer or not
        Parameters:
        - name (str) : name of the parameter
        - value (int) : value to be checked
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0 and (name == 'width' or name == 'height'):
            raise ValueError("{} must be > 0".format(name))
        elif value < 0 and (name == 'x' or name == 'y'):
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """ get width of rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set width to value
        Args:
        value (int): value to set width to
        """
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """ get height of rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """
        set height to value
        Args:
        value (int): value to set height to
        """
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """ get x property of rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        """
        set x property to a new value
        Arg:
        value: value to set x to
        """
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """ get y property of rectangle """
        return self.__y

    @y.setter
    def y(self, value):
        """
        set y property to a new value
        Arg:
        value: value to set y to
        """
        self.integer_validator("y", value)
        self.__y = value

    def area(self):
        """ Returns area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ Prints to stdout the Rectangle instance with the char # """
        if self.__y == 0:
            print(end="")
        else:
            print('\n' * self.__y, end="")

        result = []
        for _ in range(self.__height):
            row = ' ' * self.__x + '#' * self.__width
            result.append(row)
        print('\n'.join(result))

    def __str__(self):
        """ Print the string representation of the class description """
        result = '[Rectangle] ' + '(' + str(self.id) + ') '
        result += str(self.__x) + '/' + str(self.__y) + ' - '
        result += str(self.__width) + '/' + str(self.__height)
        return result

    def update(self, *args, **kwargs):
        """
        Updates the values of the arguments of a class rectangle
        The order of update is id, width, height, x, y
        If *args or **kwargs can be utilized to update the object
        """
        if args:
            arg_count = len(args)
            if arg_count >= 1:
                self.id = args[0]
            if arg_count >= 2:
                self.width = args[1]
            if arg_count >= 3:
                self.height = args[2]
            if arg_count >= 4:
                self.x = args[3]
            if arg_count >= 5:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns the dictionary rep of class Rectangle """
        dict_t = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y,
        }
        return dict_t
