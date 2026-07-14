class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find cut through binary search 
        l = 0 
        r = len(nums) - 1
        while l < r: 
            m = (l + r)//2
            if nums[m] > nums[r]: 
                l = m+1
            else: 
                r = m
        pivot = l
        print("p", pivot)
        if target > nums[len(nums) - 1]: 
            l = 0 
        else: 
            r = len(nums) - 1
        while l <= r: 
            m = (l + r)//2
            print("i", m, "e", nums[m])
            if nums[m] == target: 
                return m
            elif nums[m] < target: 
                l = m+1
            else: 
                r = m-1
        return -1
        
