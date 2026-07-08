class Solution:
    def isValid(self, s: str) -> bool:
        open_p = "({["
        closed_p = ")}]"
        open_stack = []
        closed_stack=[]
        for i in range(len(s)): 
            if s[i] in open_p: 
                open_stack.append(s[i])
            if s[i] in closed_p: 
                if len(open_stack) == 0 or (open_p.index(open_stack.pop()) != closed_p.index(s[i])):
                    return False
        if len(open_stack) > 0 or len(closed_stack) > 0: 
            return False
        return True
