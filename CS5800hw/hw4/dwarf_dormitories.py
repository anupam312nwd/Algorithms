#!/usr/bin/env python


import sys

f = open("case2.txt", "r")
data = f.read()

# data = sys.stdin.read()

mat_lst = []
for num, line in enumerate(data.split("\n")):
    if line:
        if num == 0:
            R, C = line.split(" ")
            R, C = int(R), int(C)
        else:
            lst = line.split(" ")
            lst_int = [int(x) for x in lst]
            mat_lst.append(lst_int)

# print(mat_lst)
# print(R, C)


def gen_zero_one_lst(n):
    m = 1
    lst = [[0], [1]]

    while m < n:

        tmp_lst = []
        for ele in lst:
            tmp_ele = ele.copy()
            if ele[-1] == 0:
                ele.append(1)
            else:
                ele.append(0)

            tmp_lst.append(ele)

            if (len(tmp_ele) == 1) and (tmp_ele[-1] == 0):
                tmp_ele.append(0)
                tmp_lst.append(tmp_ele)
            if (len(tmp_ele) >= 2) and (tmp_ele[-1] == 0) and (tmp_ele[-2] == 1):
                tmp_ele.append(0)
                tmp_lst.append(tmp_ele)

        m += 1
        lst = tmp_lst

    return lst


def gen_zero_one_dict(n):
    gen_lst = gen_zero_one_lst(n)
    lst_tup = []
    for ele in gen_lst:
        lst_tup.append(tuple(ele))

    gen_dict = {}
    for ele in lst_tup:
        for term in lst_tup:
            if 2 not in [sum(x) for x in zip(ele, term)]:
                if ele not in gen_dict.keys():
                    gen_dict[ele] = [term]
                else:
                    gen_dict[ele].append(term)

    return gen_dict


gen_dict = gen_zero_one_dict(C)

# print(gen_dict)

# Initialize opt_dct
opt_dict = {}
for ele in gen_dict.keys():
    opt_dict[ele] = 0
# print(opt_dict)

# print(mat_lst)
for lst in mat_lst:
    tmp_val_dict = {}
    for key in gen_dict:
        # tmp_val_dict[key] = sum([sum(x) for x in zip(lst, key)])
        sum_ele_prod = 0
        for i in range(len(lst)):
            sum_ele_prod += lst[i] * key[i]
        tmp_val_dict[key] = sum_ele_prod

    select_max_dict = {}
    for key in gen_dict:
        for item in gen_dict[key]:
            if item not in select_max_dict.keys():
                select_max_dict[item] = [opt_dict[key] + tmp_val_dict[item]]
            else:
                select_max_dict[item].append(opt_dict[key] + tmp_val_dict[item])

    # print("tmp_val_dict : ", tmp_val_dict)
    # print("select_max_dict : ", select_max_dict)
    for key in opt_dict:
        # print("--------------------------------------------------")
        opt_dict[key] = max(select_max_dict[key])
        # print("opt_dict : ", opt_dict)


max_val = 0
for _, val in opt_dict.items():
    max_val = max(max_val, val)

print(max_val)
