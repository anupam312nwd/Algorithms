from collections import defaultdict


def return_minus_one():
    return -1


class UnionFind:
    def __init__(self):
        self.graph = defaultdict(return_minus_one)

    def add_edge(self, u, v):
        self.graph[u] = v

    def find_parent(self, u):
        if self.graph[u] == -1:
            return u
        else:
            return self.find_parent(self.graph[u])


uf = UnionFind()
uf.add_edge(2, 3)
uf.add_edge(3, 4)
uf.add_edge(5, 4)
uf.add_edge(9, 6)
uf.add_edge(8, 6)
uf.add_edge(6, 7)
uf.add_edge(1, 7)

print(uf.find_parent(6))
print(uf.find_parent(9))
print(uf.find_parent(8))
print(uf.find_parent(3))
print(uf.find_parent(2))
