class Entry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        
        if self.priority < other.priority:
            return True
        else:
            return False
        

    def __eq__(self, other):
        
        if self.priority == other.priority:
            return self.item == other.item


class PQ_UL:
    def __init__(self):
        self._L = []
        self.len = 0
    
    def __len__(self):
        return self.len
    
    def insert(self, item, priority):
        self._L.append(Entry(item, priority))
        self.len += 1
    
    def find_min(self):
        min = self._L[0]
        for i in range(1, len(self)):
            if self._L[i] < min:
                min = self._L[i]
        return min
    
    def remove_min(self):
        min_index = 0
        min = self._L[0]
        for i in range(1, len(self)):
            if self._L[i] < min:
                min = self._L[i]
                min_index = i
        self._L.pop(min_index)
        self.len -= 1
        return min
        

class PQ_OL:
    def __init__(self):
        self._L = []
        self.len = 0
    
    def __len__(self):
        return self.len
    
    def insert(self, item, priority):
        self._L.append(Entry(item, priority))
        self._L.sort(reverse = True)
        self.len += 1
    
    def find_min(self):
        return self._L[-1]
    
    def remove_min(self):
        self.len -= 1
        return self._L.pop()