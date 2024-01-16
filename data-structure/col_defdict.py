""" defaultdict: dict subclass that calls a factory function to supply missing values
    Exactly like python dict except that it does not throw KeyError when trying to access a non-existent key
"""


import sys
from collections import defaultdict

print(sys.executable)
# dict1 = dict()
dict2 = defaultdict(int)

# dict1['num'] = 1
dict2["num"] = 1
# # print(dict1)
# # print(dict2)
# # print(dict1['try'])
print(dict2["try"])

# print(dict2['key'])

names = "Anup-Abhi-Sumit-Rakvi"
name_lst = names.split("-")
print(type(name_lst))
print(name_lst)
