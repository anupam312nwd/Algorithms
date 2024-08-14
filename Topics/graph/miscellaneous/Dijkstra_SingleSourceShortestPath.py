import collections
import heapq


def Dijkstra_SingleSourceShortestPath(source, adjMatWeight):
    matrixPath = collections.defaultdict(dict)
    for x, y, weight in adjMatWeight:
        matrixPath[x][y] = weight
        matrixPath[y][x] = weight
    visited = dict()
    pq = []
    heapq.heappush(pq, (0, source))

    while pq:
        distance, node = heapq.heappop(pq)
        if node in visited:
            continue
        visited[node] = distance
        for nbr, weight in matrixPath[node].items():
            if nbr not in visited:
                heapq.heappush(pq, (visited[node] + weight, nbr))
    return visited


def getAdjMatWeight_factory():
    adjMatWeight = []
    adjMatWeight.append(['a', 'b', 6])
    adjMatWeight.append(['a', 'd', 1])
    adjMatWeight.append(['b', 'd', 2])
    adjMatWeight.append(['b', 'e', 2])
    adjMatWeight.append(['b', 'a', 6])
    adjMatWeight.append(['c', 'b', 5])
    adjMatWeight.append(['c', 'e', 5])
    adjMatWeight.append(['d', 'e', 1])
    return adjMatWeight


if __name__ == '__main__':
    adjMatWeight = getAdjMatWeight_factory()
    singleSourceShortestPaths = Dijkstra_SingleSourceShortestPath('a', adjMatWeight)
    print(singleSourceShortestPaths)
