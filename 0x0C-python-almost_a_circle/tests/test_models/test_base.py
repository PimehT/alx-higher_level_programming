#!/usr/bin/python3
# test_base.py
"""Module to test Base class"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def setUp(self):
        """ Initialization of class """
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        """ Cleanup for after each test_method """
        pass

    def test_nb_objects_private(self):
        """ check if __nb_objects is a private attr """
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))
    
    def test_nb_objects_initialized(self):
        """ check if initial value of __nb_objects is zero """
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_id_none(self):
        """Test for id=None"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_id_not_none(self):
        """Test for id not None"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b3 = Base(1024)
        self.assertEqual(b3.id, 1024)
        b4 = Base()
        self.assertEqual(b4.id, 2)


if __name__ == "__main__":
    unittest.main()
