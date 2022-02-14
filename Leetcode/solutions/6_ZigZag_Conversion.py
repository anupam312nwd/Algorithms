def convert(s: str, numRows: int) -> str:
    import math

    numCol = math.ceil(len(s) * 1.0 / (2 * numRows - 2.0)) * (numRows - 1)
    zig_mat = [["" for j in range(numCol)] for i in range(numRows)]

    i, j = 0, 0
    j_old = 0
    for c in s:

        # if i < numRows - 1 and j == j_old:
        #     zig_mat[i][j] = c
        #     i += 1
        # elif i == numRows - 1 and j == j_old:
        #     zig_mat[i][j] = c
        #     j_old -= 1
        # else:
        #     i -= 1
        #     j += 1
        #     zig_mat[i][j] = c
        # if i == 0:
        #     j_old = j

        if i < numRows - 1 and j == j_old:
            zig_mat[i][j] = c
            i += 1
        elif i == numRows - 1 and j == j_old:
            zig_mat[i][j] = c
            j_old -= 1
        elif i == 0 and j != j_old:
            zig_mat[i][j] = c
            i += 1
            j_old = j
        else:
            zig_mat[i][j] = c
            i -= 1
            j += 1

    # ret_str = ""
    # for i in range(numRows):
    #     for j in range(numCol):
    #         ret_str += zig_mat[i][j]

    # return ret_str

    return zig_mat


zig_mat = convert("PAYPALISHIRING", 3)
print(zig_mat[0])
print(zig_mat[1])
print(zig_mat[2])
