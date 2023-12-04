#!/usr/bin/python3
""" Defining a class MyList """


class MyList(list):
    """ Class MyList defined """

    def print_sorted(self):
        """ Method to sort the list and print it in ascending order """
        result = self[:]
        result.sort()
        print("{}".format(result))
