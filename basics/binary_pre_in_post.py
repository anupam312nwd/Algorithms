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


def pre_recursive(root, visited=None):
    if visited is None:
        visited = []
    if root:
        visited.append(root.val)
        pre_recursive(root.left, visited)
        pre_recursive(root.right, visited)
    return visited


def in_recursive(root, visited=None):
    if visited is None:
        visited = []
    if root:
        in_recursive(root.left, visited)
        visited.append(root.val)
        in_recursive(root.right, visited)
    return visited


def post_recursive(root, visited=None):
    if visited is None:
        visited = []
    if root:
        post_recursive(root.left, visited)
        post_recursive(root.right, visited)
        visited.append(root.val)
    return visited


def pre_iterative(root):
    stack = []
    pre_ord = []
    while True:
        if root:
            pre_ord.append(root.val)
            stack.append(root)
            root = root.left
        elif stack:
            root = stack.pop()
            root = root.right
        else:
            return pre_ord


def in_iterative(root):
    stack = []
    in_ord = []
    while True:
        if root:
            stack.append(root)
            root = root.left
        elif stack:
            root = stack.pop()
            in_ord.append(root.val)
            root = root.right
        else:
            return in_ord


def post_iterative(root):
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
    nodes = [""] * 7
    for i in range(1, 6):
        nodes[i] = Node(i)
    nodes[1].left = nodes[2]
    nodes[1].right = nodes[3]
    nodes[2].left = nodes[4]
    nodes[2].right = nodes[5]

    root = nodes[1]
    print("iterative" + "-" * 11)
    print("pre: ", pre_iterative(nodes[1]))
    print("in:  ", in_iterative(nodes[1]))
    print("post:", post_iterative(nodes[1]))
    print("recursive" + "-" * 11)
    print("pre: ", pre_recursive(nodes[1]))
    print("in:  ", in_recursive(nodes[1]))
    print("post:", post_recursive(nodes[1]))

    # graph = {1: [2, 5], 2: [3, 4]}
    # G = nx.from_dict_of_lists(graph)
    # pos = graphviz_layout(G, prog="dot")
    # nx.draw(G, pos=pos, with_labels=True, arrows=True)
    # plt.show()
