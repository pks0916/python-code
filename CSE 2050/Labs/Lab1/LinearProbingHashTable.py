from UniqueLinkedList import UniqueLinkedList

class LinearProbingHashTable:
    def __init__(self, MINBUCKETS=2, MINLOADFACTOR=0.1, MAXLOADFACTOR=0.9):
        """initiliazes linear probing hash table"""
        self.MINBUCKETS = MINBUCKETS
        self.MINLOADFACTOR = MINLOADFACTOR
        self.MAXLOADFACTOR = MAXLOADFACTOR
        self.buckets = [None] * MINBUCKETS
        self.size = 0

    def __len__(self):
        """returns number of key:value paris in hash table"""
        return self.size
    

    
    def __setitem__(self, key, value):
        """sets vale for given key in hash table"""
        index = hash(key) % len(self.buckets)
        if key in self.buckets[index]:
            self.buckets[index].add(key, value)
        else:
            self.buckets[index].add(key, value)
            self.size += 1

    def __getitem__(self, key):
        """retrieves value associated with key form hash table"""
        index = hash(key) % len(self.buckets)
        return self.buckets[index].get(key)

    def __contains__(self, key):
        """checks if given key is present in hash table"""
        index = hash(key) % len(self.buckets)
        return key in self.buckets[index]

    def pop(self, key):
        """removes item w/ specified key from hash table and returns value"""
        index = hash(key) % len(self.buckets)
        value = self.buckets[index].remove(key)
        self.size -= 1
        return value

    def get_loadfactor(self):
        """return load factor"""
        return self.size / len(self.buckets)