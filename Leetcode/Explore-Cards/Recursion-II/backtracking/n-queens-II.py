#!/usr/bin/env python


def in_range(row, col):
    return 0 <= row < n and 0 <= col < n


def change_mat_horizontal_vertical(row, col, val):
    for j in range(n):
        mat[row][j] += val
    for i in range(n):
        mat[i][col] += val


def change_mat_diagonally(row, col, val):
    for step in steps:
        new_row, new_col = row, col
        while in_range(new_row + step[0], new_col + step[1]):
            new_row += step[0]
            new_col += step[1]
            mat[new_row][new_col] += val


def change_mat_cover(row, col, val):
    change_mat_horizontal_vertical(row, col, val)
    change_mat_diagonally(row, col, val)


def is_not_attacked(row, col):
    return mat[row][col] == 0


def add_queen(row, col):
    change_mat_cover(row, col, 1)


def remove_queen(row, col):
    change_mat_cover(row, col, -1)


def backtrack_nqueens(row=0, count=0):
    for col in range(n):
        if is_not_attacked(row, col):
            add_queen(row, col)
            if row + 1 == n:
                count += 1
            else:
                count = backtrack_nqueens(row + 1, count)
            remove_queen(row, col)
    return count


if __name__ == "__main__":
    n = 10
    mat = [[0 for _ in range(n)] for _ in range(n)]
    steps = {(+1, +1), (-1, +1), (+1, -1), (-1, -1)}
    total_count = backtrack_nqueens()
    print(total_count)
