from collections import deque

import matplotlib.pyplot as plt

# import networkx as nx
import numpy as np

# from networkx.drawing.nx_agraph import graphviz_layout


class Node:
    def __init__(self, val=None, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def pre_order_recursive(root, visited=None):
    if visited is None:
        visited = []
    if root:
        visited.append(root.val)
        pre_order_recursive(root.left, visited)
        pre_order_recursive(root.right, visited)
    return visited


def in_order_recursive(root, visited=None):
    if visited is None:
        visited = []
    if root:
        in_order_recursive(root.left, visited)
        visited.append(root.val)
        in_order_recursive(root.right, visited)
    return visited


def post_order_recursive(root, visited=None):
    if visited is None:
        visited = []
    if root:
        post_order_recursive(root.left, visited)
        post_order_recursive(root.right, visited)
        visited.append(root.val)
    return visited


def pre_order_iterative(root):
    stack = []
    traversal = []
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            traversal.append(root.value)
            root = root.right
    return traversal


def in_order_iterative(root):
    stack = []
    traversal = []
    while root or stack:
        if root:
            traversal.append(root.value)
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            root = root.right
    return traversal


def post_order_iterative(root):
    stack = [root]
    post_ord = []
    while stack:
        root = stack.pop()
        post_ord.append(root.val)
        if root.left:
            stack.append(root.left)
        if root.right:
            stack.append(root.right)
    post_ord.reverse()
    return post_ord


if __name__ == "__main__":

    nodes = [Node(0)] * 7
    nodes = [Node(-1)] * 7
    for i in range(1, 6):
        nodes[i] = Node(i)
    nodes[1].left = nodes[2]
    nodes[1].right = nodes[3]
    nodes[2].left = nodes[4]
    nodes[2].right = nodes[5]

    root = nodes[1]
    print("iterative" + "-" * 11)
    print("pre: ", pre_order_iterative(nodes[1]))
    print("in:  ", in_order_iterative(nodes[1]))
    print("post:", post_order_iterative(nodes[1]))
    print("recursive" + "-" * 11)
    print("pre: ", pre_order_recursive(nodes[1]))
    print("in:  ", in_order_recursive(nodes[1]))
    print("post:", post_order_recursive(nodes[1]))

    # graph = {1: [2, 5], 2: [3, 4]}
    # G = nx.from_dict_of_lists(graph)
    # pos = graphviz_layout(G, prog="dot")
    # nx.draw(G, pos=pos, with_labels=True, arrows=True)
    # plt.show()
