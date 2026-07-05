class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        output = 0
        f = 0
        d = {}
        new = True
        while (r < len(s)):
            sub_s = s[l:r+1]
            print(sub_s)
            if (new):
                if d.get(s[r]): 
                    d[s[r]] += 1
                else: 
                    d[s[r]] = 1
                # print(s[r], d[s[r]])
            f = max(f, d[s[r]])
            print("f", f)
            if (len(sub_s) - f) <= k: 
                output = max(output, len(sub_s))
                print(output)
                r += 1
                new = True
            else: 
                d[s[l]] -= 1
                l += 1
                new = False

        return output