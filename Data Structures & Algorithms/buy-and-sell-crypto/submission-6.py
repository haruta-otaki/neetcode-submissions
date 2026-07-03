class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if (n < 2):
            return 0

        max_profit = 0 
        lowest_buy = prices[0]
        for i in range(1, n):
            if (prices[i] < lowest_buy): 
                lowest_buy = prices[i]
            if (prices[i] - lowest_buy > max_profit): 
                max_profit = prices[i] - lowest_buy
        return max_profit