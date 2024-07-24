# print all elements except last
lst = [1, 2, 3]
print(lst[:-1])

# sorting
lst = [7, 5, 2, 3]
print(sorted(lst), lst)  # does not change list
lst.sort()  # sort list in place and returns nothing
print(lst)

# list of characters 'a' to 'z'
atoz = [chr(i) for i in range(ord('a'), ord('z') + 1)]
print(atoz)
