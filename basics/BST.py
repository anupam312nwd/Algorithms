""" created on Sat Jul 11, 2020;  @author: anupam
bst
"""


class Node:
    def __init__(self, data=None):

        self.data = data
        self.left = None
        self.right = None


# insert iteratively
def bst_insert(data, root=None):
    if root is None:
        return Node(data)
    else:
        if data <= root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                bst_insert(data, root.left)
        else:
            if root.right is None:
                root.right = Node(data)
            else:
                bst_insert(data, root.right)


def bst_search(data, root, parent=None, child=None):
    """return boolean, root, parent, child
    return T/F (if found), root (node of data), parent (parent of node),
    child (0/1 whether it's left/right child of parent)
    """
    if root is None:
        return False, None, None, None
    elif data == root.data:
        return True, root, parent, child
    elif data < root.data:
        return bst_search(data, root.left, root, False)
    else:
        return bst_search(data, root.right, root, True)


def bst_delete(data, root):
    """3 cases:
    if data is at a leaf node, has one child, has two child
    - first we need to search the data and corresponding node
    """
    val, node, parent, child = bst_search(data, root)
    if not val:
        return None
    else:
        # print("root.data", root.data)
        # print(root.left)
        # print(root.right)
        # case: when root has no child
        if (node.left is None) and (node.right is None):
            node.data = None
            if child:
                print("parent.right", parent.right)
                parent.right = None
            else:
                print("parent.left", parent.left)
                parent.left = None
        # case: when root has exactly one child
        elif (node.left is None) or (node.right is None):
            node.data = None
            if child:
                parent.right = parent.right.right
            else:
                parent.left.left = parent.left.left
        # case: when root has exactly two child
        else:
            min_val, min_parent = bst_min(node.right)
            node.data = min_val
            if min_parent is None:
                if node.right.right is None:
                    node.right = None
                else:
                    node.right = node.right.right
            else:
                min_parent.left = None
        return None


def bst_traverse(root, traverse=None, check_tree=None):
    if root is None:
        return
    left_data = None
    right_data = None
    if root.left is not None:
        left_data = root.left.data
    if root.right is not None:
        right_data = root.right.data
    check_tree.append([left_data, root.data, right_data])
    traverse.add(root.data)
    bst_traverse(root.left, traverse, check_tree)
    bst_traverse(root.right, traverse, check_tree)
    return traverse, check_tree


def bst_in_order_traverse(root, traverse=None):
    pass


def bst_min(root, parent=None):
    if root.left is None:
        return root.data, parent
    else:
        return bst_min(root.left, root)


def bst_max(root):
    if root.right is None:
        return root.data
    else:
        return bst_min(root.right)


if __name__ == "__main__":

    root = bst_insert(12)
    bst_insert(5, root)
    bst_insert(14, root)
    bst_insert(3, root)
    bst_insert(7, root)
    bst_insert(13, root)
    bst_insert(17, root)
    bst_insert(16, root)
    bst_insert(20, root)
    bst_insert(15, root)
    bst_insert(18, root)
    bst_insert(1, root)
    bst_insert(6, root)
    bst_insert(11, root)

    traverse, check_tree = bst_traverse(root, set(), [])
    print(traverse)
    print(check_tree)

    print("-------------------------------------------------- ")
    val, parent = bst_min(root.right)
    print(val)
    print(parent)
    bst_delete(14, root)
    traverse, check_tree = bst_traverse(root, set(), [])
    print(traverse)
    print(check_tree)
    print("-------------------------------------------------- ")
    bst_delete(7, root)
    traverse, check_tree = bst_traverse(root, set(), [])
    print(traverse)
    print(check_tree)
