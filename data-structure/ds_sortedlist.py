from sortedcontainers import SortedList

sl = SortedList([10, 12, 15, 17])
print(len(sl))
print("----------------------------------")
print(sl.bisect_left(13))
print(sl.bisect_left(14))
print(sl.bisect_left(16))
print("----------------------------------")
print(sl.bisect_right(13))
print(sl.bisect_right(14))
print(sl.bisect_right(16))
print("----------------------------------")
print(sl.bisect_left(23))
print(sl.bisect_right(23))
