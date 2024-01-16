""" [2020-07-12 Sun]
"""

from BST import bst_insert, bst_traverse

def bst_parents(root, parents=None):
    pass


def bst_height(root, height=None):
    if root is None:
        height[root] = -1
        # return
    elif (root.left is None) and (root.right is None):
        height[root] = 0
    elif (root.left is None):
        height[root] = 1
    elif (root.right is None):
        height[root] = 1
        # return
    else:
        height[root] = max(bst_height(root.right, height)[root.right], bst_height(root.left, height)[root.left]) + 1
      # return
    return height


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

print('-------------------------------------------------- ')
height = bst_height(root, height={})
print(height[root])
print('--------------------------------------------------')
print([(root.data, height[root]) for root in height])
sort_heights = sorted(height.items(), key=lambda x:x[1], reverse=True)
for root in sort_heights:
    # print(root[0].data, root[1])
    print("{:4} {:3}".format(root[0].data, root[1]))
# print(height.items())
