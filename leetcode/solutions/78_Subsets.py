#!/usr/bin/env python


def subsets(nums):

    n = len(nums)
    lst = [[]]
    output = [[]]
    temp_lst = []

    while len(lst[0]) <= n:
        temp_lst = lst.copy()
        for i in range(n):
            for s in lst:
                st = s.copy()
                if nums[i] not in st:
                    st.append(nums[i])
                else:
                    continue
                if st:
                    st.sort()
                if st not in temp_lst:
                    temp_lst.append(st)
        output += temp_lst
        lst = temp_lst.copy()

    return output


print(subsets([1, 2, 3]))
