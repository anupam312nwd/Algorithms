#!/usr/bin/env python

import time

start_time = time.time()


def fib(n, cache=None):
    if cache is None:
        cache = dict()
    if n <= 1:
        return n
    if n in cache:
        return cache[n]
    cache[n] = fib(n - 1, cache) + fib(n - 2, cache)
    return cache[n]


print(fib(444))
print(f"time-taken: {time.time() - start_time}")
