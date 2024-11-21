class Graph:
    def __init__(self):
        """Initializes a new graph"""
        raise NotImplementedError

    def connected(self, v1, v2):
        """Checks to see if there is a path from v1 to v2"""
        visited = set()
        queue = Queue()
        queue.enqueue(v1)

        while not queue.is_empty():
            vertex = queue.dequeue()
            if vertex == v2:
                return True
            visited.add(vertex)
            for neighbor in self.neighbors(vertex):
                if neighbor not in visited:
                    queue.enqueue(neighbor)
        return False

    def bfs(self, v):
        """Does a breadth first search from v"""
        visited = {}
        queue = Queue()
        queue.enqueue(v)
        visited[v] = None

        while not queue.is_empty():
            vertex = queue.dequeue()
            for neighbor in self.neighbors(vertex):
                if neighbor not in visited:
                    visited[neighbor] = vertex
                    queue.enqueue(neighbor)
        return visited

    def dfs(self, v):
        """Does a depth first search starting from v"""
        visited = {}
        stack = Stack()
        stack.push(v)
        visited[v] = None

        while not stack.is_empty():
            vertex = stack.pop()
            for neighbor in self.neighbors(vertex):
                if neighbor not in visited:
                    visited[neighbor] = vertex
                    stack.push(neighbor)
        return visited

    def shortest_path(self, v1, v2):
        """Finds the shortest path from v1 to v2"""
        from collections import deque
        queue = deque([v1])
        parents = {v1: None}
        distances = {v1: 0}
        while queue:
            current = queue.popleft()
            if current == v2:
                path = []
                step = v2
                while step is not None:
                    parent = parents[step]
                    if parent is not None:
                        path.append((parent, step))
                    step = parent
                return distances[v2], path[::-1]
            for neighbor in self.neighbors(current):
                if neighbor not in distances:
                    parents[neighbor] = current
                    distances[neighbor] = distances[current] + 1
                    queue.append(neighbor)

        return float("inf"), None

    def has_cycle(self):
        """Checks if the graph has any cycles"""
        visited = {}
        stack = Stack()
        for vertex in self:
            if vertex not in visited:
                stack.push((vertex, None))
                while not stack.is_empty():
                    current, parent = stack.pop()
                    if current in visited:
                        if visited[current] != parent:
                            return True, self._find_cycle(current, parent, visited)
                        continue
                    visited[current] = parent
                    for neighbor in self.neighbors(current):
                        if neighbor != parent:
                            stack.push((neighbor, current))
        return False, None

    def _find_cycle(self, start, parent, visited):
        """Finds the cycles in the graph"""
        cycle = []
        current = start
        while current != parent:
            prev = visited[current]
            cycle.append((prev, current))
            current = prev
        cycle.append((parent, start))
        return cycle[::-1] if cycle else []

class AdjacencySetGraph(Graph):
    def __init__(self, V=set(), E=set()):
        """Initializes an adjacency set graph"""
        self._graph = {v: set() for v in V}
        for u, v in E:
            self.add_edge(u, v)

    def __iter__(self):
        """Runs an iterator for all vertices in the graph"""
        return iter(self._graph)

    def add_vertex(self, v):
        """Adds a vertex, v, to the graph"""
        if v not in self._graph:
            self._graph[v] = set()

    def add_edge(self, u, v):
        """Adds an edge from u to v to the graph"""
        if u in self._graph:
            self._graph[u].add(v)
        else:
            self._graph[u] = {v}
        if v not in self._graph:
            self._graph[v] = set()

    def neighbors(self, v):
        """Runs an iterator for all neighbors of v"""
        return iter(self._graph.get(v, []))

class EdgeSetGraph(Graph):
    def __init__(self, V=set(), E=set()):
        """Initializes an edge set graph"""
        self._vertices = V
        self._edges = set(E)

    def __iter__(self):
        """Runs an iterator for all vertices in the graph"""
        return iter(self._vertices)

    def add_vertex(self, v):
        """Adds a vertex, v"""
        self._vertices.add(v)

    def add_edge(self, u, v):
        """Adds an edge from u to v"""
        self._edges.add((u, v))
        self._vertices.update([u, v])

    def neighbors(self, v):
        """Runs an iterator for all neighbors of v"""
        return (to for from_, to in self._edges if from_ == v)

class Queue:
    def __init__(self):
        """Initializes a queue"""
        self._head = 0
        self._L = []

    def enqueue(self, item):
        """Adds an item to the queue"""
        self._L.append(item)

    def peek(self):
        """Puts an item to the front of the queue"""
        return self._L[self._head]

    def dequeue(self):
        """Removes and returns an item from the front of the queue"""
        item = self.peek()
        self._head += 1
        if self._head > len(self._L) // 2:
            self._L = self._L[self._head:]
            self._head = 0
        return item

    def __len__(self):
        """Returns the number of items in the queue"""
        return len(self._L) - self._head

    def is_empty(self):
        """Checks if the queue is empty"""
        return len(self) == 0
    
class Stack:
    def __init__(self):
        """Initializes a stack"""
        self._L = []

    def push(self, item):
        """Pushes an item to the end of the stack"""
        self._L.append(item)

    def pop(self):
        """Removes and returns an item from the stack"""
        try:
            return self._L.pop()
        except IndexError:
            print("You cannot pop from an empty stack.")

    def peek(self):
        """Returns the item from the top of the stack"""
        return self._L[-1]

    def __len__(self):
        """Returns the number of items in the stack"""
        return len(self._L)

    def is_empty(self):
        """Checks if the stack is empty"""
        return len(self) == 0