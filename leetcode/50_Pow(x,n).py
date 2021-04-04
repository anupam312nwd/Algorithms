#!/usr/bin/env python


def myPow(x, n):

    if n < 0:
        n = -n
        x = 1 / x

    max_pow = div_power_of_2(n)

    dct_pow_2 = {0: 1, 1: 2}
    dct_pow_x = {0: x}

    for i in range(1, max_pow + 1):
        dct_pow_2[i + 1] = dct_pow_2[i] * 2
        dct_pow_x[i] = dct_pow_x[i - 1] * dct_pow_x[i - 1]

    output = 1
    while n != 0:
        max_pow = div_power_of_2(n)
        output *= dct_pow_x[max_pow]
        n = n - dct_pow_2[max_pow]

    return output


def div_power_of_2(num):
    i = 0
    while num != 1:
        num = num // 2
        i += 1
    return i


print(myPow(2.0, 10))
