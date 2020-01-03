def dfs(g):
    val = 3
    return dfs_visit(g, val)

def dfs_visit(g, val):
    return val + g

print(dfs(4))
