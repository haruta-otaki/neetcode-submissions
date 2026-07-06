class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # use this st
        if len(s1) > len(s2):
            return False
        str1 = "".join(sorted(s1)) 

        l = 0
        r = len(str1)-1
        while (r < len(s2)): 
            str2 = "".join(sorted(s2[l:r+1]))
            if str1 in str2: 
                return True
            l+=1
            r+=1
        return False


        
