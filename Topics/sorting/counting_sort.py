"""
Notes: for sorting integers only

algorithm:
- find min and max of a given array
- create an array of size max-min+1 <- counting
- count frequency of each value and store
- expand that array
"""


def counting_sort(arr):
    min_val = min(arr)
    max_val = max(arr)
    countArray = [0] * (max_val - min_val + 1)
    for value in arr:
        countArray[value - min_val] += 1

    index = 0
    for i, count in enumerate(countArray):
        if count > 0:
            for j in range(index, count + index):
                arr[j] = i + min_val
        index = count + index


if __name__ == '__main__':
    arr = [-2, -3, 9, 8, 15, 7, 0]
    counting_sort(arr)
    print('sorted array: ', arr)
