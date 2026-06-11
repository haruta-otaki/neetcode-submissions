class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # On^2 where you check every possible pair 
        n = len(heights)
        maximum = 0
        for i in range(n): 
            for j in range(i+1, n):
                total = min(heights[i], heights[j]) *  (j - i)
                if maximum < total: 
                    maximum = total
                    
        return maximum