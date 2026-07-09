class MinStack:
    def __init__(self):
        self.stack = []
        self.heap = []
        self.min_e = sys.maxsize

    def push(self, val: int) -> None:
        if val < self.min_e: 
            self.min_e = val
        self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack) == 1: 
            self.stack.pop()
            self.min_e = sys.maxsize
        elif self.stack[-1] == self.min_e:
            self.stack.pop() 
            self.min_e = min(self.stack)
        else:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_e

        
