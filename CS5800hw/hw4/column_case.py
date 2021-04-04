#!/usr/bin/env python


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


# gen_lst = gen_zero_one_lst(6)
# print(gen_lst)
# print(len(gen_lst))

gen_dict = gen_zero_one_dict(3)
print(gen_dict)

print("--------------------------------------------------")
for key in gen_dict:
    print(key, type(key))
