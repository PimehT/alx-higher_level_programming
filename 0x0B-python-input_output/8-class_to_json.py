#!/usr/bin/python3
# 8-class_to_json.py
""" returns the dictionary description of an object """


def class_to_json(obj):
    """ Converts class instance to a JSON serializable dictionary """
    return obj.__dict__
