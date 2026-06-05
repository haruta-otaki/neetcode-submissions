class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # set, sort, check consecutiveness from min with a for loop
        # track multiple list of consecutive sequences 
        # counter array 
        s = sorted(set(nums))
        #check edge cases! 
        if (len(s) == 0):
            return 0 
        print(s)
        output = [1] * len(s)
        for i in range(1, len(s)): 
            if s[i] != s[i-1] +1:                 
                output[i] = 1
            else: 
                output[i] = output[i-1] + 1
        print(output)
        return max(output)