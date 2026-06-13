class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # On^2 where you check every possible pair 
        n = len(heights)
        maximum = 0
        a = 0
        b = n - 1
        for i in range(n): 
            if b <= a: 
                break
            print(a, b, heights[a], heights[b])
            current = min(heights[a], heights[b]) * (b - a)
            if current > maximum: 
                maximum = current
            if heights[a] > heights[b]:
                b -= 1
            else: 
                a += 1
                    
        return maximum