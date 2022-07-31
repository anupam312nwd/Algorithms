#!/usr/bin/env python

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from binarytree import Node

plt.figure(figsize=(12, 12))


def pre_order_recur(root, visited=None):
    if visited is None:
        visited = []
    if root is None:
        return
    visited.append(root.value)
    pre_order_recur(root.left, visited)
    pre_order_recur(root.right, visited)
    return visited


def in_order_recur(root, visited=None):
    if visited is None:
        visited = []
    if root is None:
        return
    in_order_recur(root.left, visited)
    visited.append(root.value)
    in_order_recur(root.right, visited)
    return visited


def post_order_recur(root, visited=None):
    if visited is None:
        visited = []
    if root is None:
        return
    post_order_recur(root.left, visited)
    post_order_recur(root.right, visited)
    visited.append(root.value)
    return visited


def pre_order_iter(root):
    stack = [root]
    traversal_pre = []
    while stack:
        vertex = stack.pop()
        traversal_pre.append(vertex.value)
        if vertex.right:
            stack.append(vertex.right)
        if vertex.left:
            stack.append(vertex.left)
    return traversal_pre


# def in_order_iter(root):
#     stack = [root]
#     traversal_pre = []
#     while stack:
#         vertex = stack[-1]
#         if vertex.right:
#             stack.append(vertex.right)
#         stack.pop()
#         traversal_pre.append(vertex.value)
#         if vertex.left:
#             stack.append(vertex.left)
#     return traversal_pre


def post_order_iter(root):
    stack = [root]
    traversal_pre = []
    while True:
        if root:
            vertex = stack.pop()
        elif stack:
            stack.append(vertex.right)
        else:
            return traversal_pre


def test_traversal(root):
    assert ["a", "b", "d", "e", "f", "c"] == pre_order_recur(root)
    assert ["d", "b", "f", "e", "a", "c"] == in_order_recur(root)
    assert ["d", "f", "e", "b", "c", "a"] == post_order_recur(root)
    print(f"All traversal run successfully!")


def create_sample_tree():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    e.left = f
    return a


if __name__ == "__main__":
    root = create_sample_tree()
    print(root)
    print(f"Pre order recur: {pre_order_recur(root)}")
    print(f"Pre order iter: {pre_order_iter(root)}")
    print("--------------------------------------------------")
    print(f"In order recur: {in_order_recur(root)}")
    # print(f"In order iter: {in_order_iter(root)}")
    print("--------------------------------------------------")
    print(f"Post order recur: {post_order_recur(root)}")
    # print(f"Post order iter: {post_order_iter(root)}")
    # test_traversal(root)
