class HeapPQ:
    def __init__(self):
        self._L = []
    
    def __len__(self):
        return len(self._L)
    def _parent(self, i):
        return (i-1)//2 if i != 0 else None
    def _left(self, i):
        return 2*i + 1
    def _right(self, i):
        return 2*i + 2
    def _child(self, i):
        left = self._left(i)
        right = self._right(i)
        return range(left, min(len(self), right + 1))
        
    def put(self, item, priority):
        self._L.append((item, priority))
        self._upheap(len(self)-1)
    
    def _upheap(self, index):
        """Performs up-heap operation to maintain heap property after insertion."""
        L = self._heap
        parent = (index - 1) // 2
        if index > 0 and L[index] > L[parent]:
            L[index], L[parent] = L[parent], L[index]
            self._upheap(parent)
    def _downheap(self, index):
        """Performs down-heap operation to maintain heap property after removal."""
        L = self._heap
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        largest = index

        if left_child < len(L) and L[left_child] > L[largest]:
            largest = left_child
        if right_child < len(L) and L[right_child] > L[largest]:
            largest = right_child

        if largest != index:
            L[index], L[largest] = L[largest], L[index]
            self._downheap(largest)
            
    def remove_max(self):
        if len(self) == 0:
            raise RuntimeError
        item = self._L[0][0]
        self._L[0] = self._L[-1]
        self._l.pop()
        self._downheap(0)
        return item