#!/usr/bin/env python


def largestVariance(s: str) -> int:
    def maxSubArray(nums):
        ans = 0
        for num in nums:
            ans = max(num, num + ans)
        return max(0, ans - 1)

    f = set()
    a = ""
    for x in s:
        if x not in f:
            a += x
            f.add(x)

    n = len(s)
    res = 0
    for j in range(len(a) - 1):
        for k in range(j + 1, len(a)):
            x = a[j]
            y = a[k]
            arr = []
            for i in range(n):
                if s[i] != x and s[i] != y:
                    continue
                elif s[i] == x:
                    arr.append(1)
                else:
                    arr.append(-1)
            res = max(res, maxSubArray(arr), maxSubArray([-x for x in arr]))

    return res


if __name__ == "__main__":
    s = "baaaa"
    res = largestVariance(s)
    print(res)
