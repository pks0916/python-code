import unittest
from doublylinkedlist import Node, DoublyLinkedList


class TestNode(unittest.TestCase):
    def test_init(self):
        node = Node(5)
        self.assertEqual(node.data, 5)
        self.assertIsNone(node.prev)
        self.assertIsNone(node.link)

    def test_eq(self):
        node1 = Node(5)
        node2 = Node(5)
        self.assertEqual(node1, node2)
        node3 = Node(10)
        self.assertNotEqual(node1, node3)

    def test_repr(self):
        node = Node(5)
        self.assertEqual(repr(node), 'Node(5)')


class TestDoublyLinkedList(unittest.TestCase):
    def test_init_empty(self):
        my_list = DoublyLinkedList()
        self.assertIsNone(my_list._head)
        self.assertIsNone(my_list._tail)

    def test_init_starting_vals(self):
        my_list = DoublyLinkedList(range(10))
        current = my_list._head
        for i in range(10):
            self.assertEqual(current.data, i)
            current = current.link

    def test_add_first(self):
        my_list = DoublyLinkedList()
        my_list.add_first(5)
        self.assertEqual(my_list._head.data, 5)
        self.assertEqual(my_list._tail.data, 5)

    def test_add_last(self):
        my_list = DoublyLinkedList()
        my_list.add_last(5)
        self.assertEqual(my_list._head.data, 5)
        self.assertEqual(my_list._tail.data, 5)

    def test_remove_first(self):
        my_list = DoublyLinkedList(range(10))
        my_list.remove_first()
        self.assertEqual(my_list._head.data, 1)

    def test_remove_last(self):
        my_list = DoublyLinkedList(range(10))
        my_list.remove_last()
        self.assertEqual(my_list._tail.data, 8)

    def test_add_remove_combination(self):
        my_list = DoublyLinkedList()
        my_list.add_first(5)
        my_list.add_last(10)
        my_list.remove_first()
        my_list.add_last(15)
        my_list.remove_last()
        self.assertEqual(my_list._head.data, 5)
        self.assertEqual(my_list._tail.data, 5)

    def test_errors(self):
        my_list = DoublyLinkedList()
        with self.assertRaises(ValueError):
            my_list.remove_first()
        with self.assertRaises(ValueError):
            my_list.remove_last()


if __name__ == '__main__':
    unittest.main()