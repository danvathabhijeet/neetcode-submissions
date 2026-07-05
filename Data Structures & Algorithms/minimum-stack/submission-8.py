class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.cmin = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append([val,self.cmin])
        
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]

