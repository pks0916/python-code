import unittest
from magicsort import linear_scan, MagicCase, INVERSION_BOUND, reverse_list, magic_insertionsort, magic_mergesort, magic_quicksort, magicsort

class TestLinearScan(unittest.TestCase):
    def test_sorted(self):
        L = [1, 2, 3, 4, 5]
        self.assertEqual(linear_scan(L), MagicCase.SORTED)
    
    def test_reverse(self):
        L = [5, 4, 3, 2, 1]
        self.assertEqual(linear_scan(L), MagicCase.REVERSE_SORTED)

    def test_general(self):
        L = [3, 1, 2, 5, 4, 5, 2, 3, 4, 5, 7, 8, 0, 9, 6, 5, 2, 4, 3, 2, 5, 7, 2, 8, 0]
        self.assertEqual(linear_scan(L), MagicCase.GENERAL)
    
    def test_fewer_than_10_inversions(self):
        L = [1, 2, 4, 3, 5]
        self.assertEqual(linear_scan(L), MagicCase.CONSTANT_NUM_INVERSIONS)

class TestReverseList(unittest.TestCase):
    def test_reverse_list(self):
        input_list = [1, 2, 3, 4, 5]
        reverse_list(input_list)
        self.assertEqual(input_list, [5, 4, 3, 2, 1])

class TestMagicInsertionSort(unittest.TestCase):
    def test_insertion_sort_partial(self):
        
        L = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        magic_insertionsort(L, left=2, right=6)  # Sort from index 2 to index 5
        self.assertEqual(L, [9, 8, 4, 5, 6, 7, 3, 2, 1, 0])
    def test_insertion_sort_random_list(self):
        
        L = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        magic_insertionsort(L, left=0, right=len(L))
        self.assertEqual(L, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

class TestMagicMergeSort(unittest.TestCase):
    def test_merge_sort_partial(self):
        
        L = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        magic_mergesort(L, left=2, right=6)  
        self.assertEqual(L, [9, 8, 4, 5, 6, 7, 3, 2, 1, 0])
    



class TestMagicQuickSort(unittest.TestCase):
    def test_quick_sort_partial(self):
        
        L = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        magic_quicksort(L, left=2, right=8)  
        self.assertEqual(L, [9, 8, 2, 3, 4, 5, 6, 7, 1, 0])
    def test_quick_sort_random_list(self):
        
        L = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        magic_quicksort(L, left=0, right=len(L))
        self.assertEqual(L, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

class TestMagicSort(unittest.TestCase):
    def test_reverse_sorted_list(self):
        
        L = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        alg_set = magicsort(L)
        self.assertEqual(alg_set, {'reverse_list'})
        self.assertEqual(L, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_partial_sorted_list(self):
        
        L = [1, 2, 4, 3, 5]
        alg_set = magicsort(L)
        self.assertEqual(alg_set, {'magic_insertionsort'})
        self.assertEqual(L, [1, 2, 3, 4, 5])

    def test_complex_list(self):
        
        L = list(range(10)) + list(reversed(range(10,100)))
        alg_set = magicsort(L)
        expected_alg_set = {'magic_quicksort', 'magic_mergesort', 'magic_insertionsort'}
        self.assertEqual(alg_set, expected_alg_set)
        self.assertEqual(L, list(range(100)))

if __name__ == '__main__':
    unittest.main()
