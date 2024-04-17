"""
Notes: for sorting integers only

algorithm:
- find min and max of a given array
- create an array of size max-min+1 <- counting
- count frequency of each value and store
- expand that array

outArray[countArray[inArr[i]-min_val]-1] = inArr[i]
"""


def counting_sort(inArr):
    min_val = min(inArr)
    max_val = max(inArr)
    countArray = [0] * (max_val - min_val + 1)
    for value in inArr:
        countArray[value - min_val] += 1

    for i in range(1, len(countArray)):
        countArray[i] += countArray[i - 1]

    index = 0
    outArr = [0] * len(inArr)
    # for i in range(len(inArr) - 1, -1, -1):
    for i in range(len(inArr)):
        outArr[countArray[inArr[i] - min_val] - 1] = inArr[i]
        countArray[inArr[i] - min_val] -= 1
    return outArr


if __name__ == '__main__':
    arr = [-2, -3, 9, 8, 15, 7, 0, -4, 5]
    sortArr = counting_sort(arr)
    print('sorted array: ', sortArr)
