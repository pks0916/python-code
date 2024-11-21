import unittest
from Labs.Lab1.linkedlist import Node
import unittest
from Labs.Lab1.linkedlist import LinkedList

class testNode(unittest.TestCase):
    def test_link_list(self):
        item = "Test Item"
        link = Node("Next Node")
        node = Node(item, link)
        
        self.assertEqual(node.item, item)
        self.assertEqual(node.link, link)


class TestNodeRepresentation(unittest.TestCase):
    def test_repr(self):
        item = "Test Item"
        node = Node(item)
        
        self.assertEqual(repr(node), f"Node({item})")


class testlinkedlist(unittest.TestCase):
    def test_empty_initialization(self):
        LL1 = LinkedList()
        assert len(LL1) == 0
        assert LL1.get_head() is None
        assert LL1.get_tail() is None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        # Implement the logic to return the length of the linked list
        return len(self)

    def get_head(self):
        # Implement the logic to return the head node
        r

    def get_tail(self):
        # Implement the logic to return the tail node
        pass

class TestLinkedList:
    def test_add_last(self):
        LL1 = LinkedList()
        for i in range(1, 6):
            LL1.add_last(i)
            assert len(LL1) == i
            assert LL1.get_head().value == 1
            assert LL1.get_tail().value == i

class LinkedList:
    def add_last(self, value):
        # Implement the logic to add a node to the end of the linked list
        pass

class TestLinkedList:
    def test_non_empty_initialization(self):
        LL1 = LinkedList(['a', 'b', 'c'])
        assert len(LL1) == 3
        assert LL1.get_head().value == 'a'
        assert LL1.get_tail().value == 'c'

class LinkedList:
    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            for item in iterable:
                self.add_last(item)

class TestLinkedList:
    def test_add_first(self):
        LL1 = LinkedList()
        for i in range(1, 6):
            LL1.add_first(i)
            assert len(LL1) == i
            assert LL1.get_head().value == i
            assert LL1.get_tail().value == 1

class LinkedList:
    def add_first(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

class TestLinkedList:
    def test_remove_first(self):
        LL1 = LinkedList(['a', 'b', 'c', 'd'])
        values = ['a', 'b', 'c', 'd']
        for value in values:
            assert LL1.remove_first() == value
            values.pop(0)
            assert len(LL1) == len(values)
            if len(values) > 0:
                assert LL1.get_head().value == values[0]
                assert LL1.get_tail().value == 'd' # tail remains same
            else:
                assert LL1.get_head() is None
                assert LL1.get_tail() is None
        assert LL1.remove_first() is None  # assert remove_first() on empty list returns None

class LinkedList:
    def remove_first(self):
        if self.head is None:
            return None
        else:
            value = self.head.value
            if self.head is self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            return value
class TestLinkedList:
    def test_remove_last(self):
        LL1 = LinkedList(['a', 'b', 'c', 'd'])
        values = ['a', 'b', 'c', 'd']
        for value in reversed(values):
            assert LL1.remove_last() == value
            values.pop()
            assert len(LL1) == len(values)
            if len(values) > 0:
                assert LL1.get_tail().value == values[-1]
                assert LL1.get_head().value == 'a'  # head remains same
            else:
                assert LL1.get_head() is None
                assert LL1.get_tail() is None
        assert LL1.remove_last() is None  # assert remove_last() on empty list returns None

class LinkedList:
    def remove_last(self):
        if self.head is None:
            return None
        elif self.head is self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
            return value
        else:
            current = self.head
            while current.next is not self.tail:
                current = current.next
            value = self.tail.value
            current.next = None
            self.tail = current
            return value
      

if __name__ == '__main__':
    unittest.main()