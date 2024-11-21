import unittest
from bubblesort import bubblesort
from selectionsort import selectionsort
from insertionsort import insertionsort
# from mergesort import mergesort
# from quicksort import quicksort
import random
random.seed(658)

class SortingTestFactory:
    def setUp(self, sorting_alg):
        """Child class specifies sorting_alg to use"""
        self.sorting_alg = sorting_alg

    def assertSorts(self, L):
        """Verifies sorting alg works on L"""
        L_expected = sorted(L[:])
        self.sorting_alg(L)
        self.assertEqual(L, L_expected)

    def test_empty(self):
        """Verifies sorting alg works on empty list"""
        L = []
        self.assertSorts(L)

    def test_one(self):
        """Verifies sorting alg works on list with 1 element"""
        L = [3]
        self.assertSorts(L)

    def test_random(self):
        """Tests on 10 random lists of 100 items"""
        n = 100
        n_trials = 10
        for trial in range(n_trials):
            L = [random.randint(0, n) for i in range(n)]
            self.assertSorts(L)

    def test_arbitrarysize(self):
        """Tests that we work on lists of arbitrary size"""
        max_size = 100
        for n in range(max_size):
            L = [random.randint(0, n) for i in range(n)]
            self.assertSorts(L)

    def test_sorted(self):
        """Tests on a sorted list"""
        n = 100
        L = [i for i in range(n)]
        self.assertSorts(L)

    def test_reversed(self):
        """Tests on a reverse sorted list"""
        n = 100
        L = [n-i for i in range(n)]
        self.assertSorts(L)
    
class TestBubble(SortingTestFactory, unittest.TestCase):
    """Tests bubble ort"""
    def setUp(self):
        return SortingTestFactory.setUp(self, bubblesort)
    
class TestSelection(SortingTestFactory, unittest.TestCase):
    """Tests selectionsort"""
    def setUp(self):
        return SortingTestFactory.setUp(self, selectionsort)
    
class TestInsertion(SortingTestFactory, unittest.TestCase):
    """Tests insertionsort"""
    def setUp(self):
        return SortingTestFactory.setUp(self, insertionsort)
    
# class TestMerge(SortingTestFactory, unittest.TestCase):
#     """Tests mergesort"""
#     def setUp(self):
#         return SortingTestFactory.setUp(self, mergesort)
    
# class TestQuick(SortingTestFactory, unittest.TestCase):
#     """Tests quicksort"""
#     def setUp(self):
#         return SortingTestFactory.setUp(self, quicksort)
    
if __name__ == '__main__':
    unittest.main()