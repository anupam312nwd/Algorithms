#!/usr/bin/env python

def threeSum(nums):

    positive_lst = sorted([num for num in nums if num>=0])
    negative_lst = sorted([abs(num) for num in nums if num<=0])
    pos_hash_dict = get_hash_table(positive_lst)
    neg_hash_dict = get_hash_table(negative_lst)
    solution_set = []
    for abs_num in negative_lst:
        print(abs_num)
        lst = [list(tup) + [abs_num] for tup in pos_hash_dict[abs_num]]
        solution_set.append(lst)
    for abs_num in positive_lst:
        lst = [list(tup) + [-abs_num] for tup in neg_hash_dict[-abs_num]]
        solution_set.append(lst)
    return solution_set


def get_hash_table(nums):
    hash_table = {}
    for i in range(len(nums)):
        for j in range(i):
            if (nums[i]+nums[j]) in hash_table:
                hash_table[nums[i]+nums[j]].add((nums[i], nums[j]))
            else:
                hash_table[nums[i]+nums[j]] = {(nums[i], nums[j])}
    return hash_table


sol_set = threeSum([-2, 1, -1, 0, 3, -3])
print(sol_set)
