import collections
import math


def FloydWarshall_AllPairsShortestPath_T(adjMatWeight):
    matrixPath = collections.defaultdict(lambda: math.inf)
    nodes = set()
    for x, y, weight in adjMatWeight:
        matrixPath[(x, y)] = weight
        nodes.add(x)
        nodes.add(y)
    nodes = list(nodes)
    n = len(nodes)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                start = nodes[j]
                mid = nodes[i]
                end = nodes[k]
                if (i == j) or (i == k):
                    continue
                if (j == k):
                    matrixPath[(start, end)] = 0
                    continue
                matrixPath[(start, end)] = min(
                    matrixPath[(start, end)],
                    matrixPath[(start, mid)] + matrixPath[(mid, end)])
    return matrixPath


def FloydWarshall_AllPairsShortestPath_D(adjMatWeight):
    matrixPath = collections.defaultdict(lambda: collections.defaultdict(lambda: math.inf))
    for x, y, weight in adjMatWeight:
        matrixPath[x][y] = weight
    nodes = list(matrixPath.keys())
    n = len(nodes)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                start = nodes[j]
                mid = nodes[i]
                end = nodes[k]
                if (i == j) or (i == k):
                    continue
                if (j == k):
                    matrixPath[start][end] = 0
                    continue
                matrixPath[start][end] = min(
                    matrixPath[start][end],
                    matrixPath[start][mid] + matrixPath[mid][end])
    return matrixPath


def getAdjMatWeight_factory():
    adjMatWeight = []
    adjMatWeight.append([1, 2, 3])
    adjMatWeight.append([1, 4, 7])
    adjMatWeight.append([2, 1, 8])
    adjMatWeight.append([2, 3, 2])
    adjMatWeight.append([3, 1, 5])
    adjMatWeight.append([3, 4, 1])
    adjMatWeight.append([4, 1, 2])
    return adjMatWeight


def FloydWarshallTestAlgo():
    matrixPathSol = {(1, 2): 3, (1, 4): 6, (2, 1): 5, (2, 3): 2, (3, 1): 3, (3, 4): 1, (4, 1): 2, (2, 2): 0, (1, 3): 5,
                     (2, 4): 3, (3, 2): 6, (3, 3): 0, (4, 2): 5, (4, 3): 7, (4, 4): 0, (1, 1): 0}
    adjMatWeight = getAdjMatWeight_factory()
    matrixPath = FloydWarshall_AllPairsShortestPath_T(adjMatWeight)
    return matrixPathSol.items() == matrixPath.items()


if __name__ == '__main__':
    testPass = FloydWarshallTestAlgo()
    adjMatWeight = getAdjMatWeight_factory()
    matrixPath = FloydWarshall_AllPairsShortestPath_D(adjMatWeight)
    for key, values in matrixPath.items():
        print(key, values.items())
