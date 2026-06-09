class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 2 pointers if sum larger go down if smaller go up 
        i = 0
        j = len(numbers) - 1
        for k in range(len(numbers)): 
            summation = numbers[i] + numbers[j]
            print(summation, i, j)
            if (summation > target): 
                j -= 1
            elif (summation < target): 
                i += 1
            else: 
                break
        return [i+1,j+1]