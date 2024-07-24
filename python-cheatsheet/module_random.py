import random

lst = [2, 3, 5, 1, 2]
# choice() -> return a random element from a list
print(random.choice(lst))

# randrange(stop) or randrange(start, stop[, step])
print(random.randrange(8))
print(random.randrange(0, 101, 2))
