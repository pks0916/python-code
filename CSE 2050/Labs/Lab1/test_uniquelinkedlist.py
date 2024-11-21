import unittest
import random
random.seed(658)
from Labs.Lab1.linkedlist import LinkedList as LL
from extendedlinkedlists import ReversableLinkedList as RLL, SortedLinkedList as SLL, UniqueLinkedList as ULL

class TestUniqueLinkedList(unittest.TestCase):
    def test_inheritance(self):
        """Verifies inheritance is correctly structured"""
        uLL1 = ULL()
        self.assertIsInstance(uLL1, LL)     # is a linked list
        self.assertIsInstance(uLL1, ULL)    # is a unique linked list
        self.assertNotIsInstance(uLL1, RLL) # is not a reversable linked list
        self.assertNotIsInstance(uLL1, SLL) # is not a sorted linked list

    def test_docstrings(self):
        """Checks for docstrings"""
        self.assertIsNotNone(ULL.remove_dups.__doc__)

    def test_removedups_pdf(self):
        """Test from the pdf"""
        uLL1 = ULL('dadb')
        self.assertEqual(len(uLL1), 4)
        self.assertEqual(uLL1.get_head(), 'd')
        self.assertEqual(uLL1.get_tail(), 'b')

        # remove dups, check that we get the right dictionary
        removed_dict = uLL1.remove_dups()
        expected = {'d':1, 'a':0, 'b':0}
        self.assertEqual(removed_dict, expected)

        
        # check order is as expected
        removed_L = []
        while uLL1:
            removed_L.append(uLL1.remove_first())
        self.assertEqual(removed_L, ['d', 'a', 'b'])

    def test_removedups_random(self):
        """Tests that we work in a few random situations"""
        # List with a bunch of duplicates (~1000 items, each 1-10)
        for trial in range(100):
            n = 1000
            uLL1 = ULL()
            d_added = dict()
            L_added = []
            L_unique = []   # keep track of every unique item added

            # Add a bunch of random items in sequence
            for i in range(n):
                item = random.randint(0, 10)
                if item in d_added:
                    d_added[item] += 1
                else:
                    L_unique.append(item)
                    d_added[item] = 0

                L_added.append(item)
                uLL1.add_last(item)

                # test that add_last worked as expected
                self.assertEqual(len(uLL1), i+1)
                self.assertEqual(uLL1.get_head(), L_added[0])
                self.assertEqual(uLL1.get_tail(), L_added[-1])

            # remove duplicates
            d_removed = uLL1.remove_dups()
            self.assertEqual(len(uLL1), len(d_added))
            self.assertEqual(d_removed, d_added)

            # test that order is correct        
            L_removed = []
            while uLL1:
                L_removed.append(uLL1.remove_first())
            self.assertEqual(L_removed, L_unique)
    
unittest.main()