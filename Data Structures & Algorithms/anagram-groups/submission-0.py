class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        for i in range(len(strs)):
            flag = False
            s = strs[i]
            for j in range(len(output)): 
                if(sorted(s) == sorted(output[j][0])): 
                    output[j].append(s)
                    flag = True
            if flag == False: 
                output.append([])
                output[len(output)-1].append(s)
        return output