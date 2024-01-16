"""Counter: subclass of dict obj
   hence, has all methods of dict class
"""

from collections import Counter

lst = [1, 1, 2, 5, 2, 4, 1, 7, 7, 7, 7]
tup = tuple(lst)
l = Counter(lst)
t = Counter(tup)

print(l[1])                     # count of that object
print(t.most_common(2))
print(list(t.elements()))
print(set(t.elements()))
print(tuple(t.elements()))
print(t.most_common())
print(t.most_common(2))
print(t.most_common()[:2])
