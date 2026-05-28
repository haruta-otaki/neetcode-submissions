class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create offset
        if len(nums) == 0: 
            return False 
        offset = abs(min(nums))
        k = max(nums) + (offset + 1)
        print("k", k)
        counter = [0] * k
        for i in range(len(nums)):
            print("offset", nums[i] + offset)
            counter[nums[i] + offset] += 1
        for i in range(k): 
            if counter[i] > 1: 
                return True 
        return False
# O (n + k)
            