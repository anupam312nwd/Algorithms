#!/usr/bin/env python


class Node:
    def __init__(self, val, rank=1, parent=None):
        self.val = val
        self.rank = rank
        self.parent = parent


class unionByRank:
    def find(self, x):
        while x.parent is not None:
            x = x.parent
        return x

    def union(self, x, y):
        root1 = self.find(x)
        root2 = self.find(y)
        if root1 != root2:
            if root1.rank > root2.rank:
                root2.parent = root1
            elif root1.rank < root2.rank:
                root1.parent = root2
            else:
                root1.rank += 1
                root2.parent = root1

    def IsConnected(self, x, y):
        return self.find(x) == self.find(y)


if __name__ == "__main__":
    val1 = Node(1)
    val2 = Node(2)
    val3 = Node(3)
    val4 = Node(4)

    ubr = unionByRank()
    ubr.union(val1, val3)
    print(ubr.IsConnected(val1, val3))
