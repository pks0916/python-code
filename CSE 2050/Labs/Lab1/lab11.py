

class Graph_ES:
    def __init__(self, Vs=set(), Es=set()):
        self.Vs = Vs
        self.Es = Es
        

    def __len__(self):
        return len(self.Vs)

    def add_vertex(self, v):
        self.Vs.add(v)

    def remove_vertex(self, v):
        self.Vs.remove(v)
        self.Es = {(u, w) for (u, w) in self.Es if u != v and w != v}


    def add_edge(self, e):
        self.Es.add(e)
       

    def remove_edge(self, e):
        self.Es.remove(e)
       

    def _neighbors(self, v):
        return (w for u, w in self.Es if u == v)

    def __iter__(self):
        return iter(self.Vs)
    


class Graph_AS:
    def __init__(self, Vs=set(), Es=set()):
        self.Vs = Vs
        self.Es = Es
        self.adj = {v: set() for v in Vs}
        for (u, v) in Es:
            self.adj[u].add(v)
            self.adj[v].add(u)

    def __len__(self):
        return len(self.Vs)

    def add_vertex(self, v):
        self.Vs.add(v)
        self.adj[v] = set()

    def remove_vertex(self, v):
        self.Vs.remove(v)
        del self.adj[v]
        for u in self.adj:
            self.adj[u].discard(v)

    def add_edge(self, e):
        (u, v) = e
        self.Es.add(e)
        self.adj[u].add(v)
        self.adj[v].add(u)

    def remove_edge(self, e):
        (u, v) = e
        self.Es.remove(e)
        self.adj[u].discard(v)
        self.adj[v].discard(u)

    def _neighbors(self, v):
        return self.adj[v]

    def __iter__(self):
        return iter(self.Vs)
