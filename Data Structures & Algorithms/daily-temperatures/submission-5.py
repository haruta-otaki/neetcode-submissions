class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = [0] * n
        flag = False

        for i in range(n-2, -1, -1):
            j = i + 1
            while temperatures[j] <= temperatures[i]: 
                if output[j] == 0: 
                    flag = True
                    break

                j += output[j]
            if not flag: 
                output[i] = j - i
            else: 
                flag = False
        return output