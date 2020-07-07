""" to check whether a string is permutation of another """

import numpy as np

str1 = input("input string 1: ")
str2 = input("input string 2: ")

def checkPermutation(str1, str2):

    arr1 = np.zeros(128)
    arr2 = np.zeros(128)

    for c in str1:
        index = ord(c)
        arr1[index] += 1

    for c in str2:
        index = ord(c)
        arr2[index] += 1

    return (arr1 == arr2).all()


if __name__ == "__main__":

    val = checkPermutation(str1, str2)
    print(val)
    if val:
        print("one string is a permutation of another")
    else:
        print("one string is NOT a permutation of another")

# print(arr1)
# print(arr2)
# print(arr2 == arr1)
