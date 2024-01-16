#!/usr/bin/env python


def tower_of_hanoi(n, u, v, w, lst):
    if n == 1:
        lst.append((u, v))
        return
    tower_of_hanoi(n - 1, u, w, v, lst)
    tower_of_hanoi(1, u, v, w, lst)
    tower_of_hanoi(n - 1, w, v, u, lst)
    return lst


def tower_of_hanoi_simpler(n, u, v, w, lst):
    if n == 0:
        pass
    else:
        tower_of_hanoi_simpler(n - 1, u, w, v, lst)
        lst.append((u, v))
        tower_of_hanoi_simpler(n - 1, w, v, u, lst)


lst1 = []
lst2 = []
tower_of_hanoi(4, "A", "B", "C", lst1)
tower_of_hanoi_simpler(4, "A", "B", "C", lst2)

print(lst1)
print(lst1 == lst2)
