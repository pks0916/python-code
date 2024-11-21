import unittest
from find_factors import find_factors

class Testfactor(unittest.TestCase):
    def testfind_factor(self):
        nums = [6,7,18,1,3]
        result = {6:[6,1,3],7:[7,1],18:[6,18,1,3],1:[1],3:[1,3]}
        self.assertEqual(find_factors(nums), result)

    def test_empty(self):
        self.assertEqual(find_factors([]), {})

    def test_dup(self):
        nums = [1, 1, 1, 1, 1]
        result = {1:[1, 1, 1, 1, 1]}
        self.assertEqual(find_factors(nums), result)



unittest.main()