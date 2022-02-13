""" EASY: Best time to buy and sell stocks """

def maxProfit(self, prices):
    n = len(prices)

    Profit = 0
    for i in range(0, n):
        if prices[i] < prices[i+1]:
            Profit += prices[i+1] - prices[i]
    return Profit
