def binary_search_less_or_equal(target, arr):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] <= target:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return arr[result] if result >= 0 else -1


def binary_search_greater_or_equal(target, arr):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] >= target:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return arr[result] if result >= 0 else -1


if __name__ == '__main__':
    arr = [3, 4, 7, 10, 12, 15]
    print(binary_search_less_or_equal(2, arr))
    print(binary_search_less_or_equal(3, arr))
    print(binary_search_less_or_equal(5, arr))
    print(binary_search_less_or_equal(14, arr))
    print(binary_search_less_or_equal(17, arr))

    print('--------------------------')
    print(binary_search_greater_or_equal(2, arr))
    print(binary_search_greater_or_equal(3, arr))
    print(binary_search_greater_or_equal(5, arr))
    print(binary_search_greater_or_equal(11, arr))
    print(binary_search_greater_or_equal(17, arr))
