def maxTotalReward(rewardValues) -> int:
    rewardValues.sort()
    ans = {0}
    for r in rewardValues:
        new_rewards = set()
        for x in ans:
            if r > x:
                new_rewards.add(x + r)
        ans.update(new_rewards)

    return max(ans)


if __name__ == '__main__':
    rewardValues = [1, 4, 6, 3, 2]
    result = maxTotalReward(rewardValues)
    print(result)
