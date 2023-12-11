import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_rectangle_id_inheritance(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

    def test_multiple_rectangle_ids(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

if __name__ == '__main__':
    unittest.main()
