#!/usr/bin/env python


def move(u, v):
    print(f"move from {u} to {v}")


def tower_of_hanoi(n, u, v, w):
    if n == 1:
        move(u, v)
        return
    tower_of_hanoi(n - 1, u, w, v)
    tower_of_hanoi(1, u, v, w)
    tower_of_hanoi(n - 1, w, v, u)


def tower_of_hanoi_simpler(n, u, v, w):
    if n == 0:
        pass
    else:
        tower_of_hanoi_simpler(n - 1, u, w, v)
        move(u, v)
        tower_of_hanoi_simpler(n - 1, w, v, u)


tower_of_hanoi(4, "A", "B", "C")
