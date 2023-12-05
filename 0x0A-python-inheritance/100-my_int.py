#!/usr/bin/pyton3
""" Defining a new class """


class MyInt(int):
    """ MyInt class defined """

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
