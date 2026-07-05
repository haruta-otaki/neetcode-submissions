class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        output = 0
        while (r <= len(s)):
            sub_s = s[l:r+1]
            f = 0
            d = {}
            # print(sub_s)
            for j in range(len(sub_s)): 
                if d.get(sub_s[j]): 
                    d[sub_s[j]] += 1
                else: 
                    d[sub_s[j]] = 1
                # print(sub_s[j], d[sub_s[j]])
                f = max(f, d[sub_s[j]])
            if (len(sub_s) - f) <= k: 
                output = max(output, len(sub_s))
                # print(output)
                r += 1
            else: 
                l += 1

        return output