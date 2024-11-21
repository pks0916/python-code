class UniqueRecursiveNode:
    def __init__(self, key, value, link=None):
        """Creates a new node with key:value pair"""
        self.key = key
        self.value = value
        self.link = link

    def __iter__(self):
        """Iterates over the linked list"""
        yield self.key, self.value                      # yield values from this node
        if self.link is not None: yield from self.link  # continue to yield from link

    def __eq__(self, other):
        """method overlooked, two nodes are equal if they have same key eve if values/links are different"""
        return self.key == other.key

    def __hash__(self):
        """method overlooked, two nodes are equal if they have same key eve if values/links are different"""
        return hash(self.key)
    
    def add(self, key, value):
        """recursively adds value, either updates value of node w/ key or adds new node w/ key:value pair, returns how many nodes were added"""
        if self.key == key:
            self.value = value
            return 0
        elif self.link is None:
            self.link = UniqueRecursiveNode(key, value, None)
            return 1
        else:
            return self.link.add(key, value)

    def get(self, key):
        """recusive implementation of returning value associated with key, KeyError if not found"""
        if self and self.key == key:
            return self.value
        if self.link is None and self.key != key:
            raise KeyError(f"key {key} not found")

    def remove(self, key):
        """recursively removes node key, returns tuple of new_link, value or returns KeyError if key not found"""
        if self.key == key:
            new_link = self.link
            value=self.value
            self=self.link
            return new_link, value
        elif self.link is None:
            raise KeyError(f"key {key} not found")
        else:
            return self.link.remove(key)

    def __contains__(self, key):
        """recusively checks linked list if key and returns True if key is found, False otherwise"""
        if self.key == key:
            return True
        elif self.link is not None:
            return key in self.link
        else:
            return False

##########################################
# DO NOT CHANGE ANYTHING BELOW THIS LINE #
##########################################
class UniqueLinkedList:
    def __init__(self, items=None):
        """Creates a new linked list with optional collection of items"""
        self._head = None
        self._len = 0

        # Sequentially add items if they were included
        if items is not None:
            for key, value in items:
                self.add(key, value)

    def __len__(self):
        """Returns number of nodes in ULL"""
        return self._len
    
    def get_head(self):
        """Returns key, value in head"""
        return (self._head.key, self._head.value) if self._head is not None else None
    
    def get_tail(self):
        """Returns key, value in tail"""
        # Edge case - empty ULL
        if len(self) == 0: return None

        # Find tail node
        tail = self._head
        while tail.link is not None:
            tail = tail.link
        
        # Return key, value pair
        return (tail.key, tail.value)
    
    def add(self, key, value):
        """Adds node with key:value pair, or updates value, as appropriate"""
        # Edge case - empty linked list
        if len(self) == 0:
            self._head = UniqueRecursiveNode(key, value)
            n_added = 1
        
        else:
            # Note how we use the return value from UniqueRecursiveNode.add()
            n_added = self._head.add(key, value)
        
        self._len += n_added
        return n_added

    def get(self, key):
        """Returns value associated with key"""
        if len(self) == 0: raise KeyError(f"key {key} not in ULL")
        return self._head.get(key)

    def remove(self, key):
        """Removes node with key and returns value"""
        if len(self) == 0: raise KeyError(f"key {key} not found")

        new_head, value = self._head.remove(key)
        self._head = new_head
        self._len -= 1
        return value

    def __contains__(self, key):
        """Returns True iff key in ULL"""
        return self._head is not None and key in self._head
    
    def __iter__(self):
        """Returns iterable over key:value pairs in ULL"""
        if self._head is not None: yield from self._head