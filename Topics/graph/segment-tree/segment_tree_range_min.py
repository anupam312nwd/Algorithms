import math


def buildSegmentTree(st, arr, si, ss, se):
    if (ss == se):
        st[si] = arr[ss]
        return st[si]
    else:
        mid = (ss + se) // 2
        st[si] = min(buildSegmentTree(st, arr, 2 * si + 1, ss, mid), buildSegmentTree(st, arr, 2 * si + 2, mid + 1, se))
        return st[si]


def getRangeMin(st, si, ss, se, qs, qe):
    # total overlap: (qs ss se qe)
    if (qs <= ss) and (se <= qe):
        return st[si]

    # no overlap: ss se qs qe, qs qe ss se
    if (qe < ss) or (se < qs):
        return math.inf

    # partial overlap
    mid = (ss + se) // 2
    return min(getRangeMin(st, 2 * si + 1, ss, mid, qs, qe),
               getRangeMin(st, 2 * si + 2, mid + 1, se, qs, qe))


def updateSegmentTree(st, si, ss, se, i, val):
    if (i < ss) or (i > se):
        return
    if (ss == i) and (se == i):
        st[si] = val
        return

    mid = (ss + se) // 2
    updateSegmentTree(st, 2 * si + 1, ss, mid, i, val)
    updateSegmentTree(st, 2 * si + 2, mid + 1, se, i, val)
    st[si] = min(st[2 * si + 1], st[2 * si + 2])


def RangeMinTest():
    array = [1, 2, 5, 6, 7]
    size = 2 * 2 ** (math.ceil(math.log(len(array), 2))) - 1
    st = [0] * size
    buildSegmentTree(st, array, 0, 0, len(array) - 1)
    print(st)
    queries = [(0, 2), (1, 3), (1, 4), (2, 4), (1, 2)]

    val = 3
    i = 0
    array[i] = val
    updateSegmentTree(st, 0, 0, len(array) - 1, i, val)
    print(st)

    for qs, qe in queries:
        try:
            print('--------------------------')
            print(min(array[qs:qe + 1]), getRangeMin(st, 0, 0, len(array) - 1, qs, qe))
            assert min(array[qs:qe + 1]) == getRangeMin(st, 0, 0, len(array) - 1, qs, qe)
        except:
            break


if __name__ == '__main__':
    RangeMinTest()
