class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bst_insert(data, root):
    if root is None:
        return Node(data)
    if data <= root.val:
        if root.left is None:
            root.left = Node(data)
        else:
            bst_insert(data, root.left)
    else:
        if root.right is None:
            root.right = Node(data)
        else:
            bst_insert(data, root.right)


def bst_delete(data, root):
    # 3 cases: node is a leaf, node has a left or right child, node has two children, node is root
    node, parent = bst_find(data, root)


def bst_find(data, root, parent=None):
    if root is None:
        return -1, None
    if root.val == data:
        return root, parent
    if root.val < data:
        return bst_find(data, root.right, root)
    else:
        return bst_find(data, root.left, root)
