import random
import unittest

from lab10 import PQ_OL, PQ_UL, Entry

random.seed(658)    # Fix the seed so it fails the same way every time if there is a bug

class TestEntry(unittest.TestCase):
    def setUp(self):
        """"""
        self.e1 = Entry("rachel", 0)
        self.e2 = Entry("jake", 1)
        self.e3 = Entry("marco", 2)
        self.e4 = Entry("cassie", 3)
        self.e5 = Entry("tobias", 4)
        self.e6 = Entry("ax", 5)

    def test_init(self):
        """Tests that initialization is called correctly"""
        self.assertEqual(self.e1.item, 'rachel')
        self.assertEqual(self.e1.priority, 0)


    def test_lt(self):
        """Tests less than operator"""
        for e in [self.e2, self.e3, self.e4, self.e5, self.e6]:
            self.assertLess(self.e1, e)

        for e in [self.e1, self.e2, self.e3, self.e4, self.e5]:
            self.assertGreater(self.e6, e)

        self.assertFalse(self.e1 < Entry("alice", 0))

    def test_eq(self):
        """Tests equality operator"""
        self.assertEqual(self.e1, Entry("rachel", 0))       # same item & priority

        self.assertNotEqual(self.e1, Entry("rachel", 1))    # same item, different priority

        self.assertNotEqual(self.e1, Entry("jake", 0))      # same item, different priority

class TestPQ_UL(unittest.TestCase):
    def test_add_remove_sequential(self):
        """Adds and removes items sequentially"""
        # Construct PQ
        n = 100
        pq = PQ_UL()
        for i in range(n):
            self.assertEqual(len(pq), i)
            pq.insert(str(i), i)

        # Removes entries one at a time
        old = pq.find_min()
        for i in range(n):
            peek = pq.find_min()
            new = pq.remove_min()
            assert new == peek
            assert old.priority <= new.priority # make sure we are removing in order
            old = new

    def test_add_remove_random(self):
        """Randomly adds, then removes, a large number of items"""
        # Construct PQ
        n = 100
        pq = PQ_UL()
        for i in range(n):
            pq.insert('pikachu', random.randint(0, n))

        # Removes entries one at a time
        old = pq.find_min()
        for i in range(n):
            peek = pq.find_min()
            new = pq.remove_min()
            assert new == peek
            assert old.priority <= new.priority # make sure we are removing in order
            old = new
        

class TestPQ_OL(unittest.TestCase):
    def test_add_remove_sequential(self):
        """Adds and removes items sequentially"""
        # Construct PQ
        n = 1000
        pq = PQ_OL()
        for i in range(n):
            self.assertEqual(len(pq), i)
            pq.insert(str(i), i)

        # Removes entries one at a time
        old = pq.find_min()
        for i in range(n):
            peek = pq.find_min()
            new = pq.remove_min()
            assert new == peek
            assert old.priority <= new.priority # make sure we are removing in order
            old = new

    def test_add_remove_random(self):
        """Randomly adds, then removes, a large number of items"""
        # Construct PQ
        n = 1000
        pq = PQ_OL()
        for i in range(n):
            pq.insert('pikachu', random.randint(0, n))

        # Removes entries one at a time
        old = pq.find_min()
        for i in range(n):
            peek = pq.find_min()
            new = pq.remove_min()
            assert new == peek
            assert old.priority <= new.priority # make sure we are removing in order
            old = new

unittest.main()