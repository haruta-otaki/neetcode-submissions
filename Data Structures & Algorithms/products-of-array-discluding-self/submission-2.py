class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product = 1
        output = [1] * n
        zeros = 0
        for i in range(n):
            if nums[i] == 0: 
                zeros += 1
                continue
            product *= nums[i]
        for i in range(n): 
            if (zeros == 1 and nums[i] != 0) or zeros > 1: 
                output[i] = 0 
            elif zeros == 1 and nums[i] == 0: 
                output[i] = product
            else :
                output[i] = product // nums[i]
        return output
