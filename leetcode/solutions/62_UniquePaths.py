#!/usr/bin/env python


def uniquepaths(m, n):
    opt = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (i, j) == (1, 1):
                opt[i][j] = 1
            else:
                opt[i][j] = opt[i - 1][j] + opt[i][j - 1]
    return opt[n][m]


print(uniquepaths(3, 7))
