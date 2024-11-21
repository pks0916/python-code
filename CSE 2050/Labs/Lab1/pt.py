def fewestcoins_dyn(amt, coins): 
    min_coins = {0:0}
    for value in range(1, amt+1):
        min_coins = (9999999)
        for c in coins:
            if c <= amt:
                min_coins = min(min_coins[value], 1 + min_coins[value-c])
    return min_coins[amt]


class LLNode:
    def __init__(self, data, link=None):
        """A linked list node"""
        self.data = data
        self.link = link
 
    #######################################################
    # All methods below should be implemented recursively #
    #######################################################
 
    def __len__(self):
        if self.link is None:
            return 1
        return 1 + len(self.link)
 
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
 
    def get_tail(self):
        """"""
        if self.link is None:
            return self.data
        else:
            return self.link.get_tail()

 
    def add_last(self, item):
        """"""
        if self.link is None:
            self.link = LLNode(item)
        else:
            self.link.add_last(item)
 
    # sum_all should return the sum of all items in the linked list
    def sum_all(self):
        """"""
        if self.link is not None:
            link_sum = self.link.sum_all()
            
        else:
            link_sum = 0
        return self.data + link_sum
 
    def contains(self, item):
        if self.data == item:
            return True
        elif self.link is None:
            return False
        else:
            return self.link.contains(item)
 
    # remove_all should remove all nodes that contain a given item
    def remove_all(self, item):
        if self.link is not None:
            self.link = self.link.remove_all(item)
        if self.data == item:
            return self.link
        return self

    def reverse(self):
        if self.link is None:
            return self
        else:
            new_head = self.link.reverse()
            self.link.link = self
            self.link = None
            return new_head
 
#########################################################
# No changes below this point - all your work should be #
# in LLNode.                                            #
#########################################################
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
    


def Bs(L, item, left=0, right=None):
    if right is None:
        right = len(L) - 1
    if L[right] == L[left]:
        return False
    median = (right + left) // 2
    if L[median] == item:
        return True
    elif item < L[median]:
        return Bs(L, item, left, median)
    else:
        return Bs(L, item, median+1, right)
    

def bs_iter(L,item):
    left = 0
    right = len(L)

    while right - left > 0:
        median = (right + left) // 2

        if item == L[median]:
            return True
        elif item < L[median]: 
            right = median
        else:
            left = median + 1
    return False




def bubble(L):
    n = len(L)
    unsorted = True
    while unsorted == True:
        unsorted = False
        for i in range(n):
            for j in range (n - 1):
                if L[i] > L[i+1]:
                    L[i], L[i+1] = L[i+1], L[i]
                    unsorted = True


def selectionsort(L):
    n = len(L)
    for i in range(n):
        min_item = i
        for j in range(i, n):
            if L[j] < L[min_item]:
                min_item = j
        L[i], L[min_item] = L[min_item], L[i]



def insertionsort(L):
    n = len(L)
    for i in range(n):
        j = i 
        while j > 0 and L[j-1] > L[j]:
            L[j-1], L[j] = L[j], L[j-1]
            j -=1 


def mergesort(L):
    if len(L) < 2:
        return 
    mid = len(L) // 2
    A = L[:mid]
    B = L[mid:]
    mergesort(A)
    mergesort(B)
    merge(A, B, L)

def merge(A, B, L):
    i = 0
    j = 0 
    while len(A) > i and len(B) > j:
        if (j == len(B)) or (i < len(A) and A[i] < B[j]):
            L[i + j] = A[i]
            i += 1
        else:
            L[i + j] = B[j]
            j += 1


def quicksort(L):
    return _quicksort(L, 0, len(L))

def _quicksort(L, left, right):
    if right - left < 2:
        return
    pivot = _partition(L, left, right)

    _quicksort(L, left, pivot)
    _quicksort(L, pivot + 1, right)

def _partition(L, left, right):
    pivot = right - 1
    i = left 
    j = pivot - 1
    while i < j:
        while L[i] < L[pivot]:
            i += 1
        while i < j and j <= pivot:
            j -= 1
        if i < j:
            L[i], L[j] = L[j], L[i]
    if L[pivot] <= L[i]:
        L[pivot], L[i] = L[i], L[pivot]
        pivot += 1
    return pivot
        
            
def quickselect(L, k):
    return _quickselect(L, k, 0, len(L))

def _quickselect(L, k, left, right):
    pivot = _partition(L, left, right)
    if k == pivot + 1:
        return L[pivot]
    elif k <= pivot:
        return _quickselect(L, k, left, pivot)
    else:
        return _quickselect(L, k, pivot + 1, right)




class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
 
    def __eq__(self, other):
        if isinstance(other, Entry):
            return self.key == other.key and self.value == other.value
        return False
 
    def __hash__(self):
        return hash(self.key)
 
class HashMap:
    def __init__(self):
        self._n_buckets = 8
        self._buckets = [[] for i in range(self._n_buckets)]
        self._len = 0
 
    def __setitem__(self, key, value):
        b_i = hash(key)
        bucket = self._buckets[b_i]
        for i in bucket:
            if i.key == key:
                i.value = value
        bucket.append(Entry(key, value))

        self._len += 1
 
    def __getitem__(self, key):
        b_i = hash(key)
        bucket = self._buckets[b_i]
        for i in bucket:
            if i.key == key:
                return i.value
        raise KeyError
 
    def __len__(self):
        return self._len
 
    def __contains__(self, key):
        b_i = hash(key)
        bucket = self._buckets[b_i]
        for i in bucket:
            if i.key == key:
                return True
        return False 
 
    def pop(self, key):
        b_i = hash(key)
        bucket = self._buckets[b_i]
        bucket_to_remove = None
        for i in bucket:
            if i.key == key:
                bucket_to_remove = i
        if bucket_to_remove is None:
            raise KeyError
        bucket.remove(bucket_to_remove)
        self._len -= 1
 
    def _rehash(self, new_size):
        new_buckest = [[] for i in range(new_size)]
        for bucket in self._buckets:
            for i in bucket:
                new_buckest_index = hash(i) % new_size
                new_buckest[new_buckest_index].append(i)
        self._buckets = new_buckest
        self._n_buckets = new_size


class HashMap:
    def __init__(self):
        self._n_buckets = 8
        self._buckets = [None] * self._n_buckets
        self._len = 0

    def _hash(self, key):
        return hash(key) % self._n_buckets

    def _resize(self, new_size):
        old_buckets = self._buckets
        self._buckets = [None] * new_size
        self._n_buckets = new_size
        self._len = 0
        for bucket in old_buckets:
            if bucket:
                for entry in bucket:
                    self.__setitem__(entry.key, entry.value)

    def __setitem__(self, key, value):
        hash_value = self._hash(key)
        while self._buckets[hash_value] is not None:
            if self._buckets[hash_value].key == key:
                self._buckets[hash_value].value = value
                return
            hash_value = (hash_value + 1) % self._n_buckets
        self._buckets[hash_value] = Entry(key, value)
        self._len += 1

        # Check load factor and resize if necessary
        if self._len > self._n_buckets // 2:
            self._resize(self._n_buckets * 2)

    def __getitem__(self, key):
        hash_value = self._hash(key)
        start_hash = hash_value
        while self._buckets[hash_value] is not None:
            if self._buckets[hash_value].key == key:
                return self._buckets[hash_value].value
            hash_value = (hash_value + 1) % self._n_buckets
            if hash_value == start_hash:  # If we looped through all slots
                break
        raise KeyError

    def __len__(self):
        return self._len

    def __contains__(self, key):
        hash_value = self._hash(key)
        start_hash = hash_value
        while self._buckets[hash_value] is not None:
            if self._buckets[hash_value].key == key:
                return True
            hash_value = (hash_value + 1) % self._n_buckets
            if hash_value == start_hash:  # If we looped through all slots
                break
        return False

    def pop(self, key):
        hash_value = self._hash(key)
        start_hash = hash_value
        while self._buckets[hash_value] is not None:
            if self._buckets[hash_value].key == key:
                value = self._buckets[hash_value].value
                self._buckets[hash_value] = None
                self._len -= 1
                return value
            hash_value = (hash_value + 1) % self._n_buckets
            if hash_value == start_hash:  # If we looped through all slots
                break
        raise KeyError

class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __eq__(self, other):
        if isinstance(other, Entry):
            return self.key == other.key and self.value == other.value
        return False

    def __hash__(self):
        return hash(self.key)