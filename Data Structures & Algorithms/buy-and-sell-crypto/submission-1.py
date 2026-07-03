class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if (n < 2):
            return 0

        profits = [0] * n
        lowest_buy = prices[0]
        for i in range(1, n):
            if (prices[i] < lowest_buy): 
                lowest_buy = prices[i]
            profits[i] = prices[i] - lowest_buy
        return max(profits)