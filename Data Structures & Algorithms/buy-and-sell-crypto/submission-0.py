class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if (n < 2):
            return 0

        max_profit = 0
        for i in range(n-1):
            for j in range(i+1, n): 
                if max_profit < prices[j] - prices[i]:
                    max_profit = prices[j] - prices[i]


        return max_profit