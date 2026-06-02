class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        products1 = []
        products2 = []
        for i in range(n): 
            products1.append(nums[i]) 
            products2.append(nums[i]) 
        output = [1] * n
        for i in range(n):
            if i != 0: 
                products1[i] *= products1[i-1]
        print("products1", products1)

        for i in range(n-1, -1, -1):
            if i != n-1: 
                products2[i] *= products2[i+1]

        print("products2", products2)
        for i in range(n):
            if i - 1 < 0: 
                product1 = 1
            else: 
                product1 = products1[i-1]
            if i + 1 > n - 1: 
                product2 = 1
            else:
                product2 = products2[i+1]
            output[i] = product1 * product2
            
        return output
