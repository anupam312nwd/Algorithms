#!/usr/bin/env python

from functools import lru_cache
import time

start_time = time.time()


@lru_cache(maxsize=100)
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(350))
print(f"time-taken: {time.time()-start_time} seconds")
