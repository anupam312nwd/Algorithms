""" to check if two strings are one edit away
where one edit correspords to:
insert, remove or replace a character in a string """

""" idea: first compare length of two strings: (if len_diff > 1, return False)
 if len_diff = 0, add char_diff in comparison of char-by-char and if char_diff > 1, return False
 if len_diff = 1, slicing and concatenation """

import numpy as np

str1 = input("type string 1: ")
str2 = input("type string 2: ")

def OneAwayDist(str1, str2):
    """ compare to check if two strings are one edit away """

    len_1 = len(str1)
    len_2 = len(str2)

    if abs(len_1 - len_2) > 1:
        return False

    elif len_1 == len_2:

        num = len_1 - np.sum(np.array(list(str1)) == np.array(list(str2)))
        if num <= 1 : return True
        else: return False

    else:
        if len_1 > len_2:
            short_str = str2
            long_str = str1
        else:
            short_str = str1
            long_str = str2

        for i in range(len(long_str)):

            if long_str[:i] + long_str[i+1:] == short_str:
                return True

        return False

if __name__ == "__main__":

    if OneAwayDist(str1, str2):
        print("both strings are one dist away")
    else:
        print("more than one dist away")
