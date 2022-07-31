#!/usr/bin/env python

from collections import deque
from binarytree import Node


def levelOrder(root):
    que = deque([[root]])
    output = []
    while que:
        nodes = que.popleft()
        output.append([node.value for node in nodes])
        new_nodes = []
        for node in nodes:
            if node.left:
                new_nodes.append(node.left)
            if node.right:
                new_nodes.append(node.right)
        if new_nodes:
            que.append(new_nodes)
    return output


def create_sample_tree():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    g = Node("g")
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    e.left = f
    c.left = g
    return a


if __name__ == "__main__":
    root = create_sample_tree()
    print(root)
    output = levelOrder(root)
    print(output)
