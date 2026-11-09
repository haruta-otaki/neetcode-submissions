class Solution:
    def checkValidString(self, s: str) -> bool:
        #put open in stack then pop when closed, keep asterisk in a list so pop at anytime, when wrong pop when right no. 
        #(**
        stack = []
        stars = []
        i = 0
        for ch in s: 
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if len(stack) > 0:
                    stack.pop()
                elif len(stars) > 0:
                    stars.pop()
                else : 
                    return False
            elif ch == '*':
                stars.append(i)
            i+=1
            
        while len(stack)>0 and len(stars)>0:
            if stack.pop() > stars.pop():
                return False
        if len(stack)>0:
            return False
        return True

