import unittest
from hw6 import bubble_sort, selection_sort, insertion_sort

class SortingTestFactory:
    """This class provides methods to generate test cases for sorting algorithms."""
    def setUp(self, sorting_alg):
        """
        Set up the sorting algorithm for testing.
        Args:
            sorting_alg (function): The sorting algorithm to be tested.
        """
        self.sorting_alg = sorting_alg

    def is_sorted(self, L):
        """ Check if a list is sorted. """
        return all(L[i] <= L[i + 1] for i in range(len(L) - 1))

    def test_empty(self):
        """Test sorting an empty list."""
        arr = []
        sorted_arr, num_swaps = self.sorting_alg(arr)
        self.assertTrue(self.is_sorted(sorted_arr))
        self.assertEqual(num_swaps, 0)

    def test_sorted(self):
        """Test sorting a sorted list."""
        arr = list(range(1, 11))
        sorted_arr, num_swaps = self.sorting_alg(arr)
        self.assertTrue(self.is_sorted(sorted_arr))
        self.assertEqual(num_swaps, 0)
    
    def test_reverse_sorted(self):
        """Test sorting a reverse sorted list."""
        arr = list(range(10, 0, -1))
        sorted_arr, num_swaps = self.sorting_alg(arr)
        self.assertTrue(self.is_sorted(sorted_arr))
        self.assertEqual(num_swaps, 45)  # for Bubble and Insertion
    
    def test_random(self):
        """Test sorting a randomly shuffled list."""
        arr = [64, 34, 25, 12, 22, 11, 90]
        sorted_arr, num_swaps = self.sorting_alg(arr)
        self.assertTrue(self.is_sorted(sorted_arr))
        self.assertEqual(num_swaps, 14)  # for Bubble and Insertion
    

class TestBubble(SortingTestFactory, unittest.TestCase):
    """Test class for the bubble sort algorithm."""

    def setUp(self):
        """Set up the bubble sort algorithm for testing."""
        super().setUp(bubble_sort)


class TestInsertion(SortingTestFactory, unittest.TestCase):
    """Test class for the insertion sort algorithm."""
    def setUp(self):
        """Set up the insertion sort algorithm for testing."""
        super().setUp(insertion_sort)

class TestSelection(SortingTestFactory, unittest.TestCase):
    """Test class for the selection sort algorithm."""

    def setUp(self):
        """Set up the selection sort algorithm for testing."""
        super().setUp(selection_sort)

    def test_reverse_sorted(self):
        """Test sorting a reverse sorted list."""
        arr = list(range(10, 0, -1))
        sorted_arr, num_swaps = selection_sort(arr)
        self.assertTrue(self.is_sorted(sorted_arr))
        self.assertEqual(num_swaps, 5)

    def test_random(self):
        """Test sorting a randomly shuffled list."""
        arr = [64, 34, 25, 12, 22, 11, 90]
        sorted_arr, num_swaps = selection_sort(arr)
        self.assertTrue(self.is_sorted(sorted_arr))
        self.assertEqual(num_swaps, 4)

if __name__ == "__main__":
    unittest.main()
