def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper


@memoize
def fib(n):
    if n in {0, 1}:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


# fib = memoize(fib)

if __name__ == "__main__":
    print(fib(44))
