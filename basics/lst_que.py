#!/usr/bin/env python

from collections import deque

lst = [1, 2, 3]
que = deque(lst)

que_dir = set(dir(que))
lst_dir = set(dir(lst))
# print(lst_dir)
# print('--------------------------------------------------')
# print(que_dir)
print('--------------------------------------------------')
print("List and Deque: ", lst_dir.intersection(que_dir))
print('--------------------------------------------------')
print("List - Deque: ", lst_dir.difference(que_dir))
print('--------------------------------------------------')
print("Deque - List: ", que_dir.difference(lst_dir))
