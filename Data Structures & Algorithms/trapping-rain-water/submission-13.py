class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        l_max = height[l] 
        r_max = height[r] 
        output = 0
        while (l <= r):
            if l_max < r_max: 
                # print("l: ", l)
                l_max = max(l_max, height[l])
                # print("plus: ", l_max - height[l])
                output += (l_max - height[l])
                l += 1
            else: 
                # print("r: ", r)
                r_max = max(r_max, height[r])
                # print("plus: ", r_max - height[r])
                output += (r_max - height[r])
                r -= 1

        return output