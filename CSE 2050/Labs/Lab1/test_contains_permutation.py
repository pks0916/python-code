import unittest
from contains_permutation import contains_permutation

"""test if permutation works (what happens with it postive case and negative case)"""

class TestContainsPermutation(unittest.TestCase):
    def test_contains_permutation_positive_case(self):
        input_str = 'abcdef'
        pattern = 'cab'
        result = contains_permutation(input_str, pattern)
        self.assertTrue(result)



    def test_contains_permutation_negative_case(self):
        input_str = 'patriots'
        pattern = 'sit'
        result = contains_permutation(input_str, pattern)
        self.assertFalse(result)
