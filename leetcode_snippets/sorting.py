#!/usr/bin/env python

nums = [2, 3, 1, 8, 7]
# sort(nums)
# nums.sort()
# nums[-1], nums[-2] = nums[-2], nums[-1]
print(nums)

# nums = nums[:1]+nums[1:].sort()
# print(nums)
temp = nums[-1]
nums[-1] = nums[-2]
nums[-2] = temp
print(nums)

import numpy as np

c = np.random.randint(0, 50, 15)
lst = []

for k in c:
    lst.append(k)

print(lst)
