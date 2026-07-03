class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        l = 0
        r = 1
        h_l= height[l]
        h_r = height[r]
        total = 0
        in_water = 0
        flag = False
        while (r < n): 
            if (height[l] <= height[r]): 
                water = (r-l-1) * min(height[l], height[r])
                # print("l: ", l, "r: ", r, "height: ", min(height[l], height[r]))
                # print("water: ", (water - in_water))
                total += (water - in_water)
                in_water = 0
                l = r
            else: 
                in_water += height[r]
                # print("in_water: ", in_water)
            r += 1
        m = l 
        l = n - 2
        r = n-1
        in_water = 0
        # print("m: ", m)
        while (l >= m): 
            if (height[r] <= height[l]): 
                water = (r-l-1) * min(height[l], height[r])
                # print("l: ", l, "r: ", r, "height: ", min(height[l], height[r]))
                # print("water: ", (water - in_water))
                total += (water - in_water)
                in_water = 0
                r = l
            else: 
                in_water += height[l]
                print("in_water: ", in_water)
            l -= 1
        
        return total