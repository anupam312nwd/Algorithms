#!/usr/bin/env python

import time

start_time = time.time()


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(40))
print(f"time-taken: {time.time()-start_time}")
