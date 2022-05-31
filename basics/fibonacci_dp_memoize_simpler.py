#!/usr/bin/env python

import time

start_time = time.time()


def fibonacci(n):
    memo = {}

    def _fibonacci(n: int) -> int:
        if n < 2:
            return n
        if n not in memo:
            memo[n] = _fibonacci(n - 1) + _fibonacci(n - 2)
        # print(memo)
        return memo[n]

    return _fibonacci(n)


end_time = time.time()

print(fibonacci(400))
print(f"time-taken: {(end_time-start_time)} s")
