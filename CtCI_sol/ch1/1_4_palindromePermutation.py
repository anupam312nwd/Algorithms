""" the idea is to store number of times each unique character is appearing,
then take %mod 2, then add them and check if the sum is greater than 1 """

import numpy as np

in_str = input("type string here: ")

def palindromePermutation(in_str):

    arr = np.zeros(128)
    in_str = in_str.replace(" ", "").lower()

    for c in in_str:
        arr[ord(c)] += 1

    arr = arr%2

    return arr.sum()

if __name__ == "__main__":

    num = palindromePermutation(in_str)
    print(num)

    if num <= 1:
        print("True: permutation of Palindrome")
    else:
        print("False: NOT a permutation of Palindrome")
