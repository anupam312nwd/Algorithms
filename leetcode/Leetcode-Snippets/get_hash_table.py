#!/usr/bin/env python

lst = sorted([2, 4, 0, 2, 3, 1, 1])
neg_lst = [1, 2, 3, 4, 5, 6, 7]


def get_hash_table(nums):
    hash_table = {}
    for i in range(len(nums)):
        for j in range(i):
            if (nums[i] + nums[j]) in hash_table:
                hash_table[nums[i] + nums[j]].add((nums[i], nums[j]))
            else:
                hash_table[nums[i] + nums[j]] = {(nums[i], nums[j])}
    return hash_table


pos_hash_dict = get_hash_table(lst)
print(pos_hash_dict)

solution_set = []
for abs_num in neg_lst:
    lst = [list(tup).append(-abs_num) for tup in pos_hash_dict[abs_num]]
    print(abs_num, lst)
    solution_set.append(lst)

print(solution_set)

for i in range(5):
    print([list(tup) + [i] for tup in pos_hash_dict[i]])
