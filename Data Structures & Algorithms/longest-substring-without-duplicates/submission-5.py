class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if (n < 1):
            return 0 

        substrings = []
        substring = ""
        i = 0
        while (i < n): 
            if (s[i] in substring): 
                # print(s[i])
                current = i
                i = current - (len(substring) - (substring.index(s[i]) + 1))
                substrings.append(substring)
                # print(i, " ", s[i])
                # print(substring)
                substring = ""
            substring += s[i]
            i += 1
        substrings.append(substring)
        ans = max(substrings, key=len, default="")
        return len(ans)

        