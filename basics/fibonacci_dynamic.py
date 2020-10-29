cache = {}


def _fib(n):
    if n not in cache.keys():
        cache[n] = fib(n)
    return cache[n]


def fib(n):
    if n < 2:
        return n
    else:
        return _fib(n - 1) + _fib(n - 2)


print(fib(44))
