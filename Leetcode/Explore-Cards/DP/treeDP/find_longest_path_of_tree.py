"""
diameter of a tree: the longest path between any two nodes
height of a node in a tree: max depth from that node as a root

for any node, find longest two heights for a node and their sum + 1 is max height using that node as a root
"""


def tree_diameter(node, parent, tree, dp):
    """
    return max_height
    """
    if dp[node] != 0:
        return dp[node]

    max_height1, max_height2 = 0, 0
    if (len(tree[node]) == 1) and (parent == tree[node][0]):
        dp[node] = 1
        return 1
    for nbr in tree[node]:
        if nbr != parent:
            height = tree_diameter(nbr, node, tree, dp)
            if max_height1 < height:
                max_height1, max_height2 = height, max_height1
            elif max_height2 < height:
                max_height2 = height
    max_diameter[0] = max(max_diameter[0], max_height1 + max_height2 + 1)
    return max_height1

    # return two max heigts


# Example usage
tree = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}

dp = {node: 0 for node in tree}
max_diameter = [0]
tree_diameter(1, -1, tree, dp)
print(max_diameter[0])  # Output: 3
