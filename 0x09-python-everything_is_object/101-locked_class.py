#!/usr/bin/python3
""" defining a new class """


class LockedClass:
    """ Locked class defined """

    def __setattr__(self, name, value):
        """ sets attribute only if name has specific value """
        if name != "first_name":
            raise AttributeError("object has no attribute {}".format(name))
        else:
            self.__dict__[name] = value
