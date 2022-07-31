#!/usr/bin/env python


def tabulation_min_difficulty_job_schedule(difficultyDays: list, d: int):
    n = len(difficultyDays)
    if n < d:
        return -1

    dp = [[float("inf") for _ in range(d)] for _ in range(n)]

    # base case
    for i in range(n):
        dp[i][d - 1] = max(difficultyDays[i:])

    for day in range(d - 2, -1, -1):
        for i in range(n - 2, -1, -1):
            print(i, n - d + day + 1)
            print(dp)
            dp[i][day] = min(
                [
                    max(difficultyDays[i : j + 1]) + dp[j + 1][day + 1]
                    for j in range(i, n - d + day + 1)
                ]
            )
    return dp


if __name__ == "__main__":
    difficultyDays = [2, 3, 4, 3, 2, 5]
    d = 3
    result = tabulation_min_difficulty_job_schedule(difficultyDays, d)
    print(result)
