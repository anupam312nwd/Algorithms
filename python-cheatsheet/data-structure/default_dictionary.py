#!/usr/bin/env python

import collections

dict = collections.defaultdict(lambda: (0,0))
# dict = collections.defaultdict(int)

dict[0] = (7,2)
# print(dict[7])
print(dict[0])
print(dict[7][0])
print(dict[7][1])
