from binarysearch import binarysearch_iter
import unittest

class TestSearchFactory:
    def setUp(self, sortingalg):
        self.sortingalg = sortingalg

    def test_empty(self):
        """Ensures our code can handle an empty list"""
        L = []
        self.assertFalse(self.sortingalg(L=L, item=0))

    def test_one(self):
        """Tests code on list with one item (good starting point)"""
        L = [7]
        self.assertFalse(self.sortingalg(L=L, item=3))
        self.assertTrue(self.sortingalg(L=L, item=7))
        self.assertFalse(self.sortingalg(L=L, item=8))

    def test_arbitrary_size(self):
        """Tests for any edge cases that pop up due to length"""
        max_size = 100
        for n in range(max_size):
            L = [i+0.1 for i in range(n)]                  # offset so we don't confuse index with value
            
            for item in range(n):                          # for every item...
                self.assertFalse(self.sortingalg(L=L, item=item))       #    Look for something a bit smaller (False)
                self.assertTrue(self.sortingalg(L=L, item=item+0.1))    #    Look for this item (True)
                self.assertFalse(self.sortingalg(L=L, item=item+0.2))   #    Look for something a bit bigger (False)

class TestBinSearchIter(TestSearchFactory, unittest.TestCase):
    """Tests iterative binary search"""
    def setUp(self):
        return TestSearchFactory.setUp(self, binarysearch_iter)

if __name__ == '__main__':
    unittest.main()