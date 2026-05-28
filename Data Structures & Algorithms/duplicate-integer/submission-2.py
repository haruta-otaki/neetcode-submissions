class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create offset
        if len(nums) == 0: 
            return False 
        offset = abs(min(nums))
        counter_size = max(nums) + (offset + 1)
        print("counter_size", counter_size)
        counter = [0] * counter_size
        for i in range(len(nums)):
            print("offset", nums[i] + offset)
            counter[nums[i] + offset] += 1
        for i in range(counter_size): 
            if counter[i] > 1: 
                return True 
        return False

            