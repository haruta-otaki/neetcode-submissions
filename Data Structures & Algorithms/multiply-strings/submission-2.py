class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        nums = "0123456789"
        n1 = 0
        n2 = 0
        for i in range(len(num1)): 
            n1 += (10 ** (len(num1) - i - 1)) * nums.index(num1[i])
        print(n1)
        for i in range(len(num2)): 
            n2 += (10 ** (len(num2) - i - 1)) * nums.index(num2[i])
        print(n2)
        return str(n1 * n2)