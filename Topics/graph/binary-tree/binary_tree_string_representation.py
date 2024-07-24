from collections import deque
import json


class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_to_parentheses_preorder(root):
    if not root:
        return "()"
    if not root.left and not root.right:
        return f"({root.val})"
    left = tree_to_parentheses_preorder(root.left)
    right = tree_to_parentheses_preorder(root.right)
    return f"({root.val}{left}{right})"


def tree_to_parentheses_inorder(root):
    if not root:
        return "()"
    if not root.left and not root.right:
        return f"({root.val})"
    left = tree_to_parentheses_inorder(root.left)
    right = tree_to_parentheses_inorder(root.right)
    return f"({left}{root.val}{right})"


def tree_to_parentheses_postorder(root):
    if not root:
        return "()"
    if not root.left and not root.right:
        return f"({root.val})"
    left = tree_to_parentheses_postorder(root.left)
    right = tree_to_parentheses_postorder(root.right)
    return f"({left}{right}{root.val})"


def serialize_to_level_order(root):
    if not root:
        return "#"
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        if node:
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("#")
    return ",".join(result)


def serialize_preorder(root):
    def dfs(node):
        if not node:
            return ["#"]
        return [str(node.val)] + dfs(node.left) + dfs(node.right)

    return ",".join(dfs(root))


def tree_to_json(root):
    if not root:
        return "null"
    return json.dumps({
        "val": root.val,
        "left": tree_to_json(root.left),
        "right": tree_to_json(root.right)
    })


if __name__ == '__main__':
    one = Tree(val=1)
    two = Tree(val=2)
    three = Tree(val=3)
    four = Tree(val=4)
    five = Tree(val=5)
    six = Tree(val=6)
    one.left = two
    one.right = four
    two.left = three
    four.left = five
    four.right = six

    print(tree_to_parentheses_preorder(one))
    print(tree_to_parentheses_inorder(one))
    print(tree_to_parentheses_postorder(one))
    print(serialize_to_level_order(one))
    print(serialize_preorder(one))
    # print(tree_to_json(one))
