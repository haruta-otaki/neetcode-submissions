class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        n = len(strs)
        for i in range(n):
            s = strs[i]
            c = [0] * 26 
            for ch in s: 
                c[ord(ch) - ord('a')] += 1
            output[tuple(c)].append(s)
        return list(output.values())