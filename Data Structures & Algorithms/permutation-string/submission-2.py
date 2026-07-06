class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # instead of sorting, compare by frequency 

        if len(s1) > len(s2):
            return False

        f_1 = [0] * 26
        f_2 = [0] * 26

        for i in range(len(s1)): 
           f_1[ord(s1[i]) - ord('a')] += 1

        l = 0
        r = len(s1)-1
        for i in range(len(s2)): 
            if i <= r: 
                f_2[ord(s2[i]) - ord('a')] += 1
            else: 
                f_2[ord(s2[i]) - ord('a')] += 1
                f_2[ord(s2[l]) - ord('a')] -= 1
                l+=1
                r+=1
            if f_1 == f_2: 
                return True 
        return False

        
