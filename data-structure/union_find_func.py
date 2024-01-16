def find(v):
    if v != parent[v]:
        parent[v] = find(parent[v])  # path-compression
    return parent[v]


def combine(u, v):
    u_rep = find(u)
    v_rep = find(v)
    if u_rep == v_rep:
        return None
    if size[u_rep] < size[v_rep]:  # union by rank
        parent[u_rep] = v_rep
        size[v_rep] += size[u_rep]
    else:
        parent[v_rep] = u_rep
        size[u_rep] += size[v_rep]


lst = ["a", "b", "c", "d", "e", "f", "g", "h"]
parent = dict()
size = dict()
for c in lst:
    parent[c] = c
    size[c] = 1

combine("a", "b")
combine("b", "c")
combine("d", "c")
combine("d", "e")
combine("e", "f")
combine("g", "h")
combine("g", "e")

for c in lst:
    print(f"representative of {c} is {find(c)}")

for c in lst:
    print(f"parent of {c} is {parent[c]}, and size: {size[c]}")

