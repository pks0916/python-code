from linkedlist import Node, LinkedList

class ReversableLinkedList(LinkedList):
    """reverses the linked list"""
    def reverse(self):
        """reverses the linked list"""
        previous = None
        current = self._head
        while current is not None:
            next_node = current.link
            current.link = previous
            current.prev = next_node
            previous = current
            current = next_node

        self._head, self._tail = self._tail, self._head

class SortedLinkedList(LinkedList):
    """sorts the linked list and when something is added puts in correct spot"""

    def add_sorted(self, item):
        """sorts the linked list and when something is added puts in correct spot"""
        new_node = Node(item)
        if self._head is None or new_node.item < self._head.item:
            new_node.link = self._head
            self._head = new_node
            self._len += 1
            if self._head.link is None:
                self._tail = self._head
            return

        current = self._head

        while current.link is not None and new_node.item >= current.link.item:
            current = current.link
        new_node.link = current.link
        current.link = new_node
        self._len += 1
        if new_node.link is None:
            self._tail = new_node
        
        
    def add_first(self, item):
        """sorts the linked list and when something is added puts in correct spot"""
        raise NotImplementedError("Use add_sorted(item) instead")
    
    def add_last(self, item):
        """sorts the linked list and when something is added puts in correct spot"""
        raise NotImplementedError("Use add_sorted(item) instead")



class UniqueLinkedList(LinkedList):
    """removes duplicates in likned list and returns a dict of number of dups"""
    def remove_dups(self):
        """removes duplicates in likned list and returns a dict of number of dups"""
        dups = {}
        seen_value = set()
        prev = None
        current = self._head
        while current is not None:
            if current.item in seen_value:
                if current.item in dups:
                    dups[current.item] += 1
                    prev.link = current.link
                    self._len -= 1
                    current = prev
                else:
                    prev.link = current.link if prev is not None else None
            else:
                dups[current.item] = 0
                seen_value.add(current.item)
                prev = current
            current = current.link

        return dups
            

    



            