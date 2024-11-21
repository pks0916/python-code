import unittest
import random
from hw6 import bubble_sort, insertion_sort, selection_sort


class SortingTestFactory:
    """This class provides methods to generate test cases for sorting algorithms."""
    def setUp(self, sorting_alg):
        """
        Set up the sorting algorithm for testing.
        Args:
            sorting_alg (function): The sorting algorithm to be tested.
        """
        self.sorting_alg = sorting_alg

    def test_empty_list(self):
        """Test with an empty list."""
        test_list = []
        sorted_list = sorted(test_list)
        self.sorting_alg(test_list)
        self.assertEqual(test_list, sorted_list)

    def test_sorted_list(self):
        """Test with a sorted list."""
        test_list = [i for i in range(1, 11)]
        sorted_list = sorted(test_list)
        self.sorting_alg(test_list)
        self.assertEqual(test_list, sorted_list)

    def test_reverse_sorted_list(self):
        """Test with a reverse sorted list."""
        test_list = [i for i in range(10, 0, -1)]
        sorted_list = sorted(test_list)
        self.sorting_alg(test_list)
        self.assertEqual(test_list, sorted_list)

    def test_random_list(self):
        """Test with a random list."""
        test_list = [random.randint(1, 1000) for _ in range(10)]
        sorted_list = sorted(test_list)
        self.sorting_alg(test_list)
        self.assertEqual(test_list, sorted_list)


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


if __name__ == "__main__":
    unittest.main()
