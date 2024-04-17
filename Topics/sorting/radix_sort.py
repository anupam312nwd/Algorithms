"""
based on counting sort using cumulative frequency
"""


def counting_sort(in_arr, exp):
    count_array = [0] * 10
    for value in in_arr:
        count_array[(value // exp) % 10] += 1

    for i in range(1, 10):
        count_array[i] += count_array[i - 1]

    out_arr = [0] * len(in_arr)
    for i in range(len(in_arr) - 1, -1, -1):  # backward since it keeps already sorted part sorted
        current = in_arr[i]
        position_in_arr = count_array[(current // exp) % 10] - 1
        out_arr[position_in_arr] = current
        count_array[(current // exp) % 10] -= 1
    return out_arr


if __name__ == '__main__':
    arr = [21, 30, 923, 86, 15, 47]
    max_val = max(arr)
    max_power_of_ten = 0
    while max_val != 0:
        max_power_of_ten += 1
        max_val = max_val // 10
    for i in range(max_power_of_ten):
        arr = counting_sort(arr, exp=10 ** i)
    print('sorted array: ', arr)
