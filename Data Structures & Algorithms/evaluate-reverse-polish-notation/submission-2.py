class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ['+', '-', '*', '/']
        stack = []
        for i in range(len(tokens)): 
            if tokens[i] in operations: 
                op1 = stack[-1]
                stack.pop()
                op2 = stack[-1]
                stack.pop()
                index = operations.index(tokens[i])
                if index == 0: 
                    stack.append(op2+op1)
                elif index == 1: 
                    stack.append(op2-op1)
                elif index == 2: 
                    stack.append(op2*op1)
                else: 
                    if (op2*op1 < 0): 
                        stack.append(-(op2//-op1))
                    else: 
                        stack.append(op2//op1)
            else: 
                stack.append(int(tokens[i]))
        return stack[-1]

