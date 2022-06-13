#!/usr/bin/env python


def find_solution(candidate):
    pass


def place(candidate):
    pass


def remove(candidate):
    pass


def is_valid(candidate):
    pass


def output(candidate):
    pass


def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return

    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)


if __name__ == "__main__":
    list_of_candidates = list()
