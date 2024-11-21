import unittest
from any_two_sum import any_two_sum

"""tests if the any two sum works both positive and negative cases"""
class TestAnyTwoSum(unittest.TestCase):
    def test_positive_case(self):
        numbers = [1, 3, 4, 5]
        total = 7
        result = any_two_sum(numbers, total)
        self.assertTrue(result)

    def test_negative_case(self):
        numbers = [1, 2, 3, 4, 5]
        total = 10
        result = any_two_sum(numbers, total)
        self.assertFalse(result)
