class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        cur_ch = ''
        cur_k = k 
        d = {}
        cur_len = 0
        i = 0
        n = 0
        reset = True
        flag = False
        while (n < len(s)):
            if (reset): 
                cur_ch = s[i]
                d[s[i]] = i
                cur_k = k 
                cur_len = 1
                reset = False
            elif s[i] == cur_ch:
                cur_len += 1
            else: 
                if cur_k > 0: 
                    cur_k -= 1
                    cur_len += 1
                else: 
                    flag = True
            # print("ch", cur_ch, "i", i, "len", cur_len, flag)
            i += 1
            if i >= len(s) or flag: 
                cur_len = min(cur_len + cur_k, len(s))
                max_len = max(max_len, cur_len) 
                i = d[cur_ch] + 1
                # print("max: ", cur_ch, max_len)
                reset = True
                n += 1
                flag = False
            
        # print("max: ", cur_ch, max_len)
        # print("max: ", cur_ch, max_len)
        return max_len



            


