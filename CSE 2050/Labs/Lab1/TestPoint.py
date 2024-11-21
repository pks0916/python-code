import unittest
from Point import Point # import class Point from file Point.py

class TestPoint(unittest.TestCase):
    def setUp(self):
        """Create some points for future tests"""
        self.p1 = Point(3, 4)
        self.p2 = Point(5, 6)

    def test_init(self):
        """Tests that points are initialied with the correct attributes"""        
        self.assertEqual(self.p1.x, 3)
        self.assertEqual(self.p1.y, 4)
        """Tests that points are initialied with the correct attributes"""        

    def test_eq(self):
        """test equal correctly"""
        self.assertEqual()
        self.assertNotEqual()
        """ADD YOUR OWN DOCSTRING"""

    def test_equidistant(self):
        """test points are equidistance from orgin"""
        self.assertEqual()
        self.assertEqual()
        self.assertNotEqual()
        """ADD YOUR OWN DOCSTRING"""

    def test_within(self):
        """test that points can be found with in a radius"""
        self.assertEqual()
        self.assertNotEqual()
        """ADD YOUR OWN DOCSTRING"""

unittest.main() # This line tells unittest to 
                #    1) create an object for every untitest.TestCase class
                #    2) Run every method that begins with 'test' in those objects
