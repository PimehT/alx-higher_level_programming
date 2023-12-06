#!/usr/bin/python3
# 11-student.py
""" defining a class called student """


class Student:
    """ class defined """

    def __init__(self, first_name, last_name, age):
        """
        Initialization of class Student
        Args:
        first_name (str): first name of student
        last_name (str): last name of student
        age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__

        student_attrs = {}
        for attr in attrs:
            if hasattr(self, attr):
                student_attrs[attr] = getattr(self, attr)
        return student_attrs

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
