class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dynamic programming 
        # +1 everytime confirmed 
        n = len(text1)
        m = len(text2)
        output = []
        for i in range(n+1): 
            row = []
            for j in range(m+1): 
                row.append(0)
            output.append(row)
                    
                    
        for i in range(n-1, -1, -1): 
            for j in range(m-1, -1, -1): 
                if text1[i] == text2[j]: 
                    output[i][j] = output[i+1][j+1] + 1
                else: 
                    output[i][j] = max(output[i+1][j], output[i][j+1])
        return output[0][0]