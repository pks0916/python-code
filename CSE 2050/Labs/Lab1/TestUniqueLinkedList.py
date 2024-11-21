import unittest, random
random.seed(658)
from UniqueLinkedList import UniqueRecursiveNode, UniqueLinkedList

class TestUniqueRecursiveNode(unittest.TestCase):
    def test_init(self):
        """Checks key:value attributes in a newUniqueRecursiveNode"""
        n1 =UniqueRecursiveNode(key=3, value='jake')
        self.assertEqual(n1.key, 3)
        self.assertEqual(n1.value, 'jake')

    def test_eq(self):
        """Checks that twoUniqueRecursiveNodes are equal iff they have the same key"""
        # Same keys
        self.assertEqual(UniqueRecursiveNode(key=1, value="jake"),UniqueRecursiveNode(key=1, value="jake"))
        self.assertEqual(UniqueRecursiveNode(key=1, value="jake"),UniqueRecursiveNode(key=1, value="rachel"))

        # different keys
        self.assertNotEqual(UniqueRecursiveNode(key=1, value="jake"),UniqueRecursiveNode(key=2, value="jake"))
        self.assertNotEqual(UniqueRecursiveNode(key=1, value="jake"),UniqueRecursiveNode(key=2, value="rachel"))

    def test_hash(self):
        """Checks that UniqueRecursiveNodes with the same key hash to the same value"""
        self.assertEqual(hash(UniqueRecursiveNode(key=1, value="jake")), hash(UniqueRecursiveNode(key=1, value="rachel")))

    # add, get, remove, contains, itertested in TestUniqueLinkedList below
        

class TestUniqueLinkedList(unittest.TestCase):
    def test_init(self):
        """Creates an empty ULL"""
        ull1 = UniqueLinkedList()
        self.assertIsNone(ull1.get_head())
        self.assertIsNone(ull1.get_tail())
        self.assertEqual(len(ull1), 0)

    def assertLLMarkers(self, ull, head, tail, length):
        """Tests that the head/tail/length of a ULL are correct"""
        self.assertEqual(ull.get_head(), head)
        self.assertEqual(ull.get_tail(), tail)
        self.assertEqual(len(ull), length)

    def test_add_remove(self):
        """Sequentially adds then removes unique key:value pairs"""
        n = 100 # number of items to add, then remove

        # Create and check empty ULL
        ull1 = UniqueLinkedList()
        self.assertLLMarkers(ull1, None, None, 0)

        # add items
        for i in range(n):
            self.assertNotIn(i, ull1)
            self.assertEqual(ull1.add(key=i, value=str(i)), 1)
            self.assertIn(i, ull1)
            self.assertEqual(ull1.get(i), str(i))
            self.assertLLMarkers(ull1, head=(0, str(0)), tail=(i, str(i)), length=i+1)

        # remove items
        for i in range(n):
            self.assertLLMarkers(ull1, head=(i, str(i)), tail=(n-1, str(n-1)), length=n-i)
            self.assertEqual(ull1.remove(i), str(i))
            self.assertNotIn(i, ull1)

        # check empty ULL
        self.assertLLMarkers(ull1, None, None, 0)

    def test_unique(self):
        """Sequentiall adds some unique and some duplicate keys, ensures length is correctly updated"""
        n = 100
        n_duplicate_adds = 10

        # Create and check empty ULL
        ull1 = UniqueLinkedList()
        self.assertLLMarkers(ull1, None, None, 0)

        # add items
        for i in range(n):
            self.assertNotIn(i, ull1)
            self.assertEqual(ull1.add(key=i, value=str(i)), 1)
            self.assertIn(i, ull1)
            expected_head = (0, str(0)) if i==0 else (0, str(n_duplicate_adds-1))
            self.assertLLMarkers(ull1, head=expected_head, tail=(i, str(i)), length=i+1)

            # Extra adds should change the value, not the length
            for j in range(n_duplicate_adds):
                self.assertEqual(ull1.add(key=i, value=str(i+j)), 0)
                self.assertIn(i, ull1)
                expected_head = (0, str(0+j)) if i==0 else (0, str(n_duplicate_adds-1))
                self.assertLLMarkers(ull1, head=expected_head, tail=(i, str(i+j)), length=i+1)

        # remove items
        for i in range(n):
            self.assertLLMarkers(ull1, head=(i, str(i+n_duplicate_adds-1)), tail=(n-1, str(n-1+n_duplicate_adds-1)), length=n-i)
            self.assertEqual(ull1.remove(i), str(i+n_duplicate_adds-1))
            self.assertNotIn(i, ull1)

        # check empty ULL
        self.assertLLMarkers(ull1, None, None, 0)

    def test_remove_exception(self):
        """Ensures we raise a key error if key not found"""
        n = 100
        ull1 = UniqueLinkedList()

        for i in range(n):
            self.assertRaises(KeyError, ull1.remove, key=i)
            ull1.add(key=i, value=str(i))

    def test_iter(self):
        """Tests that we can iterate over key:value pairs"""
        n = 100
        ull1 = UniqueLinkedList()

        for i in range(n):
            ull1.add(i, str(i))

        iter_list = [(node[0], node[1]) for node in ull1]
        iter_list_expected = [(i, str(i)) for i in range(n)]

        self.assertEqual(iter_list, iter_list_expected)

if __name__ == '__main__':
    unittest.main()