#!/usr/bin/env python

# testing priority queue

import heapq

dct = {"a": 5, "b": 3, "c": 2, "d": 4}
node = min(dct, key=dct.get)
print(node)
