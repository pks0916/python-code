import unittest
import random
random.seed(658)
from Labs.Lab1.linkedlist import LinkedList as LL
from extendedlinkedlists import ReversableLinkedList as RLL, SortedLinkedList as SLL, UniqueLinkedList as ULL

class TestSortedLinkedList(unittest.TestCase):
    def test_inheritance(self):
        """Verifies inheritance is correctly structured"""
        sLL1 = SLL()
        self.assertIsInstance(sLL1, LL)     # is a linked list
        self.assertIsInstance(sLL1, SLL)    # is a soted linked list
        self.assertNotIsInstance(sLL1, RLL) # is not a reversable linked list
        self.assertNotIsInstance(sLL1, ULL) # is not a unique linked list

    def test_docstrings(self):
        """Checks for docstrings"""
        self.assertIsNotNone(SLL.add_sorted.__doc__)
        self.assertIsNotNone(SLL.add_first.__doc__)
        self.assertIsNotNone(SLL.add_last.__doc__)

    def test_addfirstaddlastoverload(self):
        """Checks that add_first and add_last have been overloaded to raise errors"""
        sLL1 = SLL()
        self.assertRaises(NotImplementedError, sLL1.add_first, 0)
        self.assertRaises(NotImplementedError, sLL1.add_last, 0)

    def test_addsorted_pdf(self):
        """Test from the pdf"""
        sLL1 = SLL()
        
        # 8
        sLL1.add_sorted(8)
        self.assertEqual(sLL1.get_head(), 8)
        self.assertEqual(sLL1.get_tail(), 8)
        self.assertEqual(len(sLL1), 1)

        # 3-8
        sLL1.add_sorted(3)
        self.assertEqual(sLL1.get_head(), 3)
        self.assertEqual(sLL1.get_tail(), 8)
        self.assertEqual(len(sLL1), 2)

        # 3-8-11
        sLL1.add_sorted(11)
        self.assertEqual(sLL1.get_head(), 3)
        self.assertEqual(sLL1.get_tail(), 11)
        self.assertEqual(len(sLL1), 3)

        # 1-3-8-11
        sLL1.add_sorted(1)
        self.assertEqual(sLL1.get_head(), 1)
        self.assertEqual(sLL1.get_tail(), 11)
        self.assertEqual(len(sLL1), 4)

        # 1-3-8-9-11
        sLL1.add_sorted(9)
        self.assertEqual(sLL1.get_head(), 1)
        self.assertEqual(sLL1.get_tail(), 11)
        self.assertEqual(len(sLL1), 5)

        removed = []
        while sLL1:
            removed.append(sLL1.remove_first())
        
        self.assertEqual(removed, [1, 3, 8, 9, 11])

    def test_random(self):
        """Tests add_sorted with a large number of random items"""
        n = 1000

        # Build sLL1 and a sorted list L
        sLL1 = SLL()
        L = []

        for i in range(n):
            item = random.randint(0, n)
            L.append(item)
            sLL1.add_sorted(item)
        L.sort()

        # test that first and last item match
        self.assertEqual(sLL1.get_head(), L[0])
        self.assertEqual(sLL1.get_tail(), L[-1])
        self.assertEqual(len(sLL1), n)

        # Iteratively remove all items and check
        removed = []
        while sLL1:
            removed.append(sLL1.remove_first())
        
        self.assertEqual(removed, L)
    
unittest.main()