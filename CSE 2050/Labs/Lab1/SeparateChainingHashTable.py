from UniqueLinkedList import UniqueLinkedList

class SeparateChainingHashTable:
    def __init__(self, MINBUCKETS=2, MINLOADFACTOR=0.5, MAXLOADFACTOR=1.5):
        """initializes parameters for SeparateChainingHashTable class"""
        self.MINBUCKETS = MINBUCKETS
        self.MINLOADFACTOR = MINLOADFACTOR
        self.MAXLOADFACTOR = MAXLOADFACTOR
        self.buckets = [UniqueLinkedList() for _ in range(MINBUCKETS)]
        self.size = 0

    def __len__(self):
        """returns number of buckets"""
        return self.size
    
    
    def __setitem__(self, key, value):
        """adds/updates key, value pair as needed"""
        index = hash(key) % len(self.buckets)
        if key in self.buckets[index]:
            self.buckets[index].add(key, value)
        else:
            self.buckets[index].add(key, value)
            self.size += 1

    def __getitem__(self, key):
        """returns value from key or raises KeyError if not found"""
        index = hash(key) % len(self.buckets)
        bucket = self.buckets[index]
        if bucket is None:
            raise KeyError(f"Key '{key}' not found")
        return bucket[key]

    def __contains__(self, key):
        """returns true or false if found or not, respectively"""
        index = hash(key) % len(self.buckets)
        return key in self.buckets[index]

    def pop(self, key):
        """removes key: value pair and returns value that was popped or raises KeyError"""
        index = self._hash_function(key)
        bucket = self.buckets[index]
        
        if bucket is None:
            raise KeyError(key)
        
        prev = None
        current = bucket
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.buckets[index] = current.next
                self.size -= 1
                return current.value
            prev = current
            current = current.next
        
        raise KeyError(key)

    def get_loadfactor(self):
        """return load factor"""
        return self.size / len(self.buckets)