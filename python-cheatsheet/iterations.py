import itertools

moregrid = [(1, 2), (0, 1), (1, 2), (1, 0)]

for more in itertools.permutations(moregrid):
    print(more)
