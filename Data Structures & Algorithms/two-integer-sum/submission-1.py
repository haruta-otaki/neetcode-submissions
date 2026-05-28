class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        d = {}
        for i in range (n):
            if (d.get(target - nums[i]) != None):
                return [d[target - nums[i]], i]
            d[nums[i]] = i        
        return [0, 0]