import collections

ordct = collections.OrderedDict()

ordct['foo'] = 3
ordct['baz'] = 7
ordct['edc'] = 9

print(ordct.keys())

for key, val in ordct.items():
    print(key, val)
