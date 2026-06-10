class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # brute force, O(n^3) 
        s_nums = sorted(nums)
        n = len(nums)
        output = []
        # do iteration + 2 pointers 
        # do contains to avoid duplicates 
        
        for i in range(n): 
            target = (-1) * s_nums[i]
            a = i + 1
            b = n - 1
            for j in range(i+1, n):
                if (a < b): 
                    if s_nums[a] + s_nums[b] > target: 
                        b -= 1
                    elif s_nums[a] + s_nums[b] < target: 
                        a += 1
                    else: 
                        ans = [s_nums[i], s_nums[a], s_nums[b]]
                        if ans not in output: 
                            output.append(ans)
                        b-=1
        return output