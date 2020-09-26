import numpy as np

lst_a = [2, 7, 11, 22]

lst = lst_a


def change_list(lst):
    len_lst = len(lst)
    lst[0], lst[len_lst-1] = lst[len_lst-1], lst[0]


change_list(lst)
print(lst_a)
print(lst)

A = np.random.randint(0, 11, 7)
