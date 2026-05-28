class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = []
        t_list = []
        n = len(s)
        if len(s) != len(t):
            return False
        for i in range (n): 
            s_list.append(s[i])
            t_list.append(t[i])
        sorted_s = sorted(s_list)
        sorted_t = sorted(t_list)
        if (sorted_s != sorted_t):
            return False 
        return True
            