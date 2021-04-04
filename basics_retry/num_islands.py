def numIslands(grid) -> int:
    num_islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                traverse_grid(grid, i, j)
                num_islands += 1
    return num_islands


def traverse_grid(grid, i, j):
    if (
        (i < 0)
        or (j < 0)
        or (i >= len(grid))
        or (j >= len(grid[0]))
        or (grid[i][j] != "1")
    ):
        return None
    grid[i][j] = "2"
    traverse_grid(grid, i - 1, j)
    traverse_grid(grid, i, j - 1)
    traverse_grid(grid, i + 1, j)
    traverse_grid(grid, i, j + 1)


grid = [
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["1", "1", "0", "1", "1"],
]

num_row, num_column = len(grid), len(grid[0])
print(num_row, num_column)
print(numIslands(grid))
