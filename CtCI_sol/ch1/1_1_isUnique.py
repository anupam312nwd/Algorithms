""" I am using here additional data structure (namely ndarray)"""

import numpy as np

arr = np.zeros(128)
input_str = input("type a string: ")

for c in input_str:
    index = ord(c)
    arr[index] += 1

if max(arr) <= 1:
    print("input string ", input_str, "is Unique")
else:
    print("input string ", input_str, "is NOT Unique")

# print(input_str)
