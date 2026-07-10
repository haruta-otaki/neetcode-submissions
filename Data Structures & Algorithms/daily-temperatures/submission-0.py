class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        i = 0
        max_temp = -sys.maxsize
        l = 0
        r = 0
        output = []
        for i in range(len(temperatures)): 
            for j in range(i, len(temperatures) + 1):
                if j == len(temperatures): 
                    output.append(0)
                    break
                if temperatures[i] < temperatures[j]: 
                    output.append(j-i)
                    break
        return output
