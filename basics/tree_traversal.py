#!/usr/bin/env python


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_root_left_recursive(root, level=0, dct=None):
    if dct is None:
        dct = dict()
    if root:
        level += 1
        right_root_left_recursive(root.right, level, dct)
        dct[level] = dct.get(level, [])
        dct[level].append(root.val)
        right_root_left_recursive(root.left, level, dct)
        level -= 1
    return dct


def right_root_left_iterative(root, dct=None):
    if dct is None:
        dct = dict()
    stack = []
    stack.append((root, 1))
    while stack:
        root, level = stack.pop()
        dct[level] = dct.get(level, [])
        dct[level].append(root.val)
        if root.left:
            stack.append((root.left, level + 1))
        if root.right:
            stack.append((root.right, level + 1))
    return dct


if __name__ == "__main__":
    root = TreeNode(1)
    n3 = TreeNode(3)
    n2 = TreeNode(2)
    n5 = TreeNode(5)
    n4 = TreeNode(4)
    n6 = TreeNode(6)
    root.left = n3
    root.right = n2
    n3.left = n5
    n3.right = n4
    n5.left = n6

    dct = right_root_left_recursive(root)
    print(dct)
    dct = right_root_left_iterative(root)
    print(dct)
