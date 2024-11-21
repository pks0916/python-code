import unittest
import random
random.seed(658)
from Labs.Lab1.linkedlist import LinkedList as LL
from extendedlinkedlists import ReversableLinkedList as RLL, SortedLinkedList as SLL, UniqueLinkedList as ULL

class TestReversableLinkedList(unittest.TestCase):
    def test_inheritance(self):
        """Verifies inheritance is correctly structured"""
        rLL1 = RLL()
        self.assertIsInstance(rLL1, LL)     # is a linked list
        self.assertIsInstance(rLL1, RLL)    # is a reversable linked list
        self.assertNotIsInstance(rLL1, SLL) # is not a sorted linked list
        self.assertNotIsInstance(rLL1, ULL) # is not a unique linked list

    def test_docstrings(self):
        """Checks for docstrings"""
        self.assertIsNotNone(RLL.reverse.__doc__)

    def test_reverse_pdf(self):
        """Checks that we can reverse with the pdf example"""
        rLL1 = RLL('abcd')

        # before reversing
        self.assertEqual(len(rLL1), 4)
        self.assertEqual(rLL1.get_head(), 'a')
        self.assertEqual(rLL1.get_tail(), 'd')

        # reverse
        rLL1.reverse()

        # after reversing
        self.assertEqual(rLL1.get_head(), 'd')
        self.assertEqual(rLL1.get_tail(), 'a')
        self.assertEqual(len(rLL1), 4)

        # make sure items are removed correctly
        removed = []
        while rLL1:
            removed.append(rLL1.remove_first())
        
        self.assertEqual(removed, ['d', 'c', 'b', 'a'])

    def test_reverse_random(self):
        """Checks that we can reverse with a large amount of random numbers"""
        n = 100
        L = [random.randint(0, n) for i in range(n)] # large amount of random numbers

        rLL1 = RLL(L) # initially holds the same items in the same order

        # before reversing
        self.assertEqual(len(rLL1), n)
        self.assertEqual(rLL1.get_head(), L[0])
        self.assertEqual(rLL1.get_tail(), L[-1])

        # reverse
        rLL1.reverse()

        # after reversing
        self.assertEqual(rLL1.get_head(), L[-1])
        self.assertEqual(rLL1.get_tail(), L[0])
        self.assertEqual(len(rLL1), n)

        # make sure items are removed correctly
        removed = []
        while rLL1:
            removed.append(rLL1.remove_first())

        L.reverse()
        
        self.assertEqual(removed, L)

    

unittest.main()