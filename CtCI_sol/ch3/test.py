""" check for stack and queues """

from collections import deque

lst = [2, 'a', 4, 7, None, 'a', 'b', 7, None]
que = deque(lst)

que_dir = set(que.__dir__())
lst_dir = set(lst.__dir__())
# print(lst_dir)
# print(que_dir)
# print('-------------------------------------------------- ')
# print(lst_dir.intersection(que_dir))
# print(lst_dir.difference(que_dir))
# print(que_dir.difference(lst_dir))

lst1 = []
lst1.append([])
print(lst1)
lst1[0].append(1)
print(lst1)
lst1.append([])
print(lst1)

lst1.pop()
print(lst1)
lst1.pop()
print(lst1)
print('-------------------------------------------------- ')
lst2 = [[1, 2], [5, 4]]
lst2[-1].pop()
if len(lst2[-1]) == 1:
    lst2.pop()
print(lst2)
lst2[-1].pop()
lst2.append([])
print(lst2)
print(not lst2[-1])
lst2[-1].append(4)
if lst2[-1]:
    print('not empty')
    lst2[-1].pop()
    print('noW empty')

print(range(6))
print(type(range(6)))
print(list(range(6)))
print(set(range(6)))
print(tuple(range(6)))
