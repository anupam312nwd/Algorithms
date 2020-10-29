#!/usr/bin/env python

import sys
import heapq
data = sys.stdin.read()



graph = {}
for num, line in enumerate(data.split("\n")):
    if line:
        if num == 0:
            N, M, T = line.split(" ")
            N, M, T = int(N), int(M), int(T)
        else:
            x, y, t1, t2 = line.split(" ")
            x, y, t1, t2 = int(x), int(y), int(t1), int(t2)
            if x in graph.keys():
                if y in graph[x].keys():
                    graph[x][y].append((t1, t2))
                else:
                    graph[x][y] = [(t1, t2)]
            else:
                graph[x] = {y: [(t1, t2)]}

# print(graph)


# def escape_from_time(graph: dist, N: int, T: int):
def escape_from_time(graph, N, T):

    graph[N] = {}
    all_vertices = graph.keys()
    visited = {1}
    time_dict = {}
    heap = []
    not_visited = {1}

    # Initialization
    for ver in all_vertices:
        if ver != 1:
            time_dict[ver] = float("inf")
            not_visited.add(ver)
            heapq.heappush(heap, ((float("inf"), 0), (ver, ver)))
        else:
            time_dict[ver] = 0
            heapq.heappush(heap, ((0, 0), (ver, ver)))

    while not_visited and heap:
        time_tup, ver_tup = heapq.heappop(heap)
        if time_dict[ver_tup[0]] > time_tup[0] and (
            0 < time_tup[1] - time_dict[ver_tup[1]] <= T
        ):
            time_dict[ver_tup[0]] = time_tup[0]
            visited.add(ver_tup[0])

        if ver_tup[0] in not_visited:
            not_visited.remove(ver_tup[0])

        for nbr in graph[ver_tup[0]]:
            graph[ver_tup[0]][nbr].sort()
            for start_t, stop_t in graph[ver_tup[0]][nbr]:
                previous_stop_t = time_dict[ver_tup[0]]
                if previous_stop_t + T >= start_t > previous_stop_t:
                    break
            if nbr in not_visited and time_dict[nbr] > stop_t and 0 < start_t - time_dict[ver_tup[0]] <= T :
                time_dict[nbr] = stop_t
                heapq.heappush(heap, ((stop_t, start_t), (nbr, ver_tup[0])))

    # return time_dict
    return time_dict[N]

tmin = escape_from_time(graph, N, T)

if tmin < float('inf'):
    print('YES', tmin)
else:
    print('NO')

# time_dict = escape_from_time(graph, N, T)
# print(time_dict)
