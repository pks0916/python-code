import unittest
from remove_characters import remove_characters

"""test if remove charcater works (what happens with it postive case and negative case)"""
class TestRemoveCharacters(unittest.TestCase):
    def test_remove_single_character(self):
        input_str = 'abcd'
        to_remove = 'c'
        result = remove_characters(input_str, to_remove)
        self.assertEqual(result, 'abd')
    
    
    def test_remove_no_characters(self):
        input_str = 'abcd'
        to_remove = 'xyz'
        result = remove_characters(input_str, to_remove)
        self.assertEqual(result, 'abcd')