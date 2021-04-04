#!/usr/bin/env python

dct = {"a": [2, 3], "b": [3, 4], "c": [1, 0]}

# max_val = 0
# for _, val in dct.items():
#     max_val = max(max_val, val)

# print(max_val)

# for key, item in dct.items():
#     print(key, item)


# for key in dct:
#     for item in dct[key]:
#         print(key, item)

lst = [-1, 1]
key = [2, 5]

sum_elm_prod = 0
for i in range(len(lst)):
    sum_elm_prod += lst[i] * key[i]

# k = [sum(x * y) for x, y in zip(lst, key)]
t = sum([sum(x) for x in zip(lst, key)])
# print(k)
print(t)
print("--------------------------------------------------")
print(sum_elm_prod)
