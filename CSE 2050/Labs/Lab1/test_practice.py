import unittest
from calc import add, sub, div, mul

class TestingPractice(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-10, 5), -5)
        self.assertEqual(add(-10, -5), -15)

    def test_sub(self):
        self.assertEqual(sub(-10, 5), -15)
        self.assertEqual(sub(-10, -5), -5)
    
    def test_div(self):
        self.assertEqual(div(10, 5), 2)
        self.assertEqual(div(-10, 5), -2)
        self.assertEqual(div(-10, -5), 2)
        
        
        with self.assertRaises(ValueError):
            div (10,0)

    def test_mul(self):
        self.assertEqual(mul(10, 5), 50)
        self.assertEqual(mul(-10, 5), -50)
        self.assertEqual(mul(-10, -5), 50)



if __name__ == "__main__":
    unittest.main()