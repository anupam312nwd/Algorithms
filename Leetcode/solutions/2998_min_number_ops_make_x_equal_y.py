import collections

x = 1
y = 4

visited = set()
queue = collections.deque([x])

result = 0
found = False
while queue:
    next_candidates = []
    for curr in queue:
        if curr == y:
            found = True
            break
        if (curr > x + y + 5 + 11) or (curr < 0):
            continue
        if curr in visited:
            continue
        visited.add(curr)
        next_candidates.append(curr + 1)
        next_candidates.append(curr - 1)
        if curr % 11 == 0:
            next_candidates.append(curr // 11)
        if curr % 5 == 0:
            next_candidates.append(curr // 5)
    queue = next_candidates[:]
    if found == True:
        break
    result += 1

print(f'result: {result}')
