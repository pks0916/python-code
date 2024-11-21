class LLNode:
    def __init__(self, data, link=None):
        """A linked list node"""
        self.data = data
        self.link = link

    # Recursive Example:
    # recursively call on self.link until tail node
    def __len__(self):
        """Recursively calculates how many items are in LL starting at this node"""
        # base case: tail node, len = 1
        if self.link is None:
            return 1
        # recursive case: len = 1 + len(link)
        return 1 + len(self.link)

    # Recursive example:
    # has helper function to create mutable collection
    # to store state at all levels of recursion
    def __repr__(self):
        """Recursively prints all nodes"""
        return ' -> '.join(self._repr([]))

    def _repr(self, item_list):
        """
        Helper function for __repr__.
        Allows item_list to be initialized as an empty mutable.
        """
        item_list.append(f"Node({self.data})")
        # If this node is not the tail, keep adding nodes
        if self.link is not None:
            self.link._repr(item_list)
        return item_list

    # Recursive example:
    # get the last item, then pass it back through all level of recursion
    def get_tail(self):
        """Recursively gets the item stored in the tail node"""
        if self.link is None:
            return self.data
        else:
            return self.link.get_tail()

    # TODO: Implement the methods below.
    # Use recursion.
    # Non-recursive solutions will not receive credit.
    def add_last(self, item):
        if self.link is None:
            self.link = LLNode(item)
        else:
            self.link.add_last(item)

    def sum_all(self):
        if self.link is None:
            return self.data
        else:
            return self.data + self.link.sum_all()

    def contains(self, item):
        if self.data == item:
            return True
        elif self.link is None:
            return False
        else:
            return self.link.contains(item)

    def remove_all(self, item):
        if self is None:
            return None  
    
        if self.data == item:
            return self.link.remove_all(item) if self.link else None
    
        if self.link is not None:
            self.link = self.link.remove_all(item)
        return self

    def reverse(self):
        if self.link is None:
            return self
        else:
            new_head = self.link.reverse()
            self.link.link = self
            self.link = None
            return new_head


# Do not make any changes to LinkedList:
# all your code should be above in the LLNode class
class LinkedList:
    def __init__(self, items=None):
        """Initializes a new empty LinkedList"""
        self._head = None
        if items is not None:
            for item in items:
                self.add_last(item)  # use add_last() to maintain ordering

    def add_first(self, item):
        """Adds to beginning of Linked List"""
        self._head = LLNode(item, self._head)

    def remove_first(self):
        """Removes and returns first item"""
        # Edge case
        if self._head is None:
            raise RuntimeError('Cannot remove from an empty list.')
        item = self._head.data  # retrieve data
        self._head = self._head.link  # update head
        return item

    # For demonstration and debug purposes: Prints all the elements
    def __repr__(self):
        """Recursively prints the Linked List"""
        return repr(self._head)

    def __len__(self):
        """Returns the number of nodes in Linked List"""
        return len(self._head) if self._head else 0

    def __contains__(self, item):
        """Returns True if item is in Linked List. Returns False otherwise."""
        if self._head is None:
            return False
        return self._head.contains(item)

    def add_last(self, item):
        """Adds item to end of Linked List"""
        if self._head is None:
            return self.add_first(item)
        self._head.add_last(item)

    def sum_all(self):
        """Returns sum of all items in Linked List"""
        return self._head.sum_all() if self._head else 0

    def remove_all(self, item):
        """Removes all occurrences of item from Linked List"""
        if self._head is not None:
            self._head = self._head.remove_all(item)

    # Reverses the list in linear time, no copying of the data
    def reverse(self):
        """Reverses linked list"""
        # Note that LLNode.reverse() should return the new head
        if self._head is not None:
            self._head = self._head.reverse()

    def get_tail(self):
        """Returns the item stored in tail"""
        return self._head.get_tail() if self._head else None
