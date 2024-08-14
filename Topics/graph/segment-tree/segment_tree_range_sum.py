import math


def buildSegmentTree(st, arr, si, ss, se):
    if (ss == se):
        st[si] = arr[ss]
        return st[si]
    else:
        mid = (ss + se) // 2
        st[si] = buildSegmentTree(st, arr, 2 * si + 1, ss, mid) + buildSegmentTree(st, arr, 2 * si + 2, mid + 1, se)
        return st[si]


def getSumRange(st, si, ss, se, qs, qe):
    # total overlap
    if (qs <= ss) and (se <= qe):
        return st[si]

    # no overlap: ss se qs qe, qs qe ss se
    if (qe < ss) or (se < qs):
        return 0

    # partial overlap
    mid = (ss + se) // 2
    return (getSumRange(st, 2 * si + 1, ss, mid, qs, qe) +
            getSumRange(st, 2 * si + 2, mid + 1, se, qs, qe))


def updateSegmentTree(st, si, ss, se, i, diff):
    if (i < ss) or (i > se):
        return
    st[si] += diff
    if (ss != se):
        mid = (ss + se) // 2
        updateSegmentTree(st, 2 * si + 1, ss, mid, i, diff)
        updateSegmentTree(st, 2 * si + 2, mid + 1, se, i, diff)


def SumRangeTest():
    array = [1, 2, 5, 6, 7]
    size = 2 * 2 ** (math.ceil(math.log(len(array), 2)))
    st = [0] * size
    buildSegmentTree(st, array, 0, 0, len(array) - 1)
    print(st)
    queries = [(0, 2), (1, 3), (1, 4), (2, 4), (1, 2)]

    array = [1, 4, 5, 6, 7]
    diff = 2
    i = 1
    updateSegmentTree(st, 0, 0, len(array) - 1, i, diff)
    print(st)
    for qs, qe in queries:
        try:
            print('--------------------------')
            print(sum(array[qs:qe + 1]), getSumRange(st, 0, 0, len(array) - 1, qs, qe))
            assert sum(array[qs:qe + 1]) == getSumRange(st, 0, 0, len(array) - 1, qs, qe)
        except:
            break


if __name__ == '__main__':
    SumRangeTest()
