#!/usr/bin/python3
# test_rectangle.py
""" module to test the class Rectangle """


import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
import sys


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def setUp(self):
        """ Initialization of class """
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        """ Cleanup for after each test_method """
        pass

    def test_inheritance(self):
        """ Check if class inherits Base """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_constructor_insufficient_arg(self):
        """ Check what happen if arguments are not enough """
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle()
        self.assertEqual(str(e.exception), "__init__() missing 2 required positional arguments: 'width' and 'height'")

        with self.assertRaises(TypeError) as e:
            r2 = Rectangle(1)
        self.assertEqual(str(e.exception), "__init__() missing 1 required positional argument: 'height'")

    def test_constructor_sufficient_arg(self):
        """ Check attributes when there are two args"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_constructor_multiple_arg(self):
        """ Check results of multiple args within the specified range """
        r1 = Rectangle(1, 1, 1, 1, 1)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 1)

    def test_input_validator(self):
        """ Check output only for when input is not an int"""
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(10, "2")
        self.assertEqual(str(e.exception), "height must be an integer")

        with self.assertRaises(TypeError) as e:
            r2 = Rectangle({}, 2)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_input_positive(self):
        """ Check output for when width or height <= 0"""
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(10, 0)
        self.assertEqual(str(e.exception), "height must be > 0")

        with self.assertRaises(ValueError) as e:
            r2 = Rectangle(-1, 5)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_input_negative(self):
        """ Check output for when x or y is < 0"""
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(10, 2, -1)
        self.assertEqual(str(e.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as e:
            r2 = Rectangle(3, 4, 0, -5)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_area(self):
        """ Test implementation of Rectangle.area method """
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        """Test implementation of Rectangle.display method"""
        r1 = Rectangle(4, 6)
        captured_output = StringIO()
        sys.stdout = captured_output
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "####\n####\n####\n####\n####\n####\n")

        captured_output = StringIO()
        sys.stdout = captured_output
        r2 = Rectangle(2, 2)
        r2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "##\n##\n")

    def test__str__(self):
        """Test implementation of the __str__ method"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

    def test_update_no_keyword(self):
        """Test update method with no-keyword arguments"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")

        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")

        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_with_keyword(self):
        """Test update method with key-worded arguments"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/1")

        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/10 - 1/1")

        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/1")

        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")


if __name__ == '__main__':
    unittest.main()
