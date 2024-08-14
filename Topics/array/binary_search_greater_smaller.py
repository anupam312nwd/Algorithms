def binary_search_smaller_or_equal(target, arr):
    left, right = 0, len(arr)  # right taken as len(arr) instead of len(arr)-1 to cover last index
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left - 1


def binary_search_greater_or_equal(target, arr):
    # return index at which insert target such that arr remains sorted
    # if 0 <= index < len(arr), then arr[index] >= target
    left, right = 0, len(arr)  # right taken as len(arr) instead of len(arr)-1 to cover last index
    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == '__main__':
    arr = [3, 4, 7, 7, 10, 12, 12, 12, 12, 12, 15]

    print(f'arr : {arr}')
    print()
    print('binary search LESS or equal to: ----')
    queries = [2, 3, 5, 11, 17]
    result_indices = [binary_search_smaller_or_equal(target, arr) for target in queries]
    print(f'queries: {queries}')
    print(f'result_indices: {result_indices}')
    result_array = list([arr[i] if 0 <= i < len(arr) else -1 for i in result_indices])
    print(f'result array: {result_array}')
    print()

    print('binary search GREATER or equal to: ----')
    queries = [2, 3, 5, 11, 17]
    result_indices = [binary_search_greater_or_equal(target, arr) for target in queries]
    print(f'queries: {queries}')
    print(f'result_indices: {result_indices}')
    result_array = list([arr[i] if 0 <= i < len(arr) else -1 for i in result_indices])
    print(f'result array: {result_array}')
