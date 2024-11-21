class Node:
    def __init__(self, data, prev=None, link=None):
        self.data = data
        self.prev = prev
        self.link = link
        if prev is not None:
            self.prev.link = self
        if link is not None:
            self.link.prev = self

    def __eq__(self, other):
        return isinstance(other, Node) and self.data == other.data

    def __repr__(self):
        return f"Node({self.data})"


class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None

    def __len__(self):
        count = 0
        current = self._head
        while current:
            count += 1
            current = current.link
        return count

    def add_first(self, item):
        if self._head is None and self._tail is None:
            self._head = self._tail = Node(item, None, None)
        else:
            newNode = Node(item, None, self._head)
            self._head.prev = newNode
            self._head = newNode

    def add_last(self, item):
        if self._head is None and self._tail is None:
            self._head = self._tail = Node(item, None, None)
        else:
            newNode = Node(item, self._tail, None)
            self._tail.link = newNode
            self._tail = newNode

    def remove_first(self):
        if self._head is None:
            return
        if self._head == self._tail:
            self._head = self._tail = None
            return
        self._head = self._head.link
        self._head.prev = None

    def remove_last(self):
        if self._head is None:
            return
        if self._head == self._tail:
            self._head = self._tail = None
            return
        self._tail = self._tail.prev
        self._tail.link = None