#
# 2: abc, 3: def, 4: ghi, 5: jkl, 6: mno, 7: pqrs, 8: tuv, 9: wxyz

# class string_output:
#     def __init__(self, string = None):
#         pass

phone_dict = {2: {"a", "b", "c"}, 3: {"d", "e", "f"}, 4: {"g", "h", "i"},
              5: {"j", "k", "l"}, 6: {"m", "n", "o"},
              7: {"p", "q", "r", "s"}, 8: {"t", "u", "v"},
              9: {"w", "x", "y", "z"}}

num = '2345'
arr = []
arr_new = []

for i in range(len(num)):
    i = int(num[i])
    if not arr:
        for alp in phone_dict[i]:
            arr.append(alp)
        arr_new = arr
    else:
        for alp in phone_dict[i]:
            for str1 in arr:
                temp_str = str1
                temp_str = alp + temp_str
                arr_new.append(temp_str)
                # print(arr_new)

    arr = arr_new
    arr_new = []

print(arr)
