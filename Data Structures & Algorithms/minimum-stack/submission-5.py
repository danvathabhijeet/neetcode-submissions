class MinStack:

    def __init__(self):
        self.stack = []
        self.mstack = []
        self.minval = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mstack or self.mstack[-1] > val:
            self.minval = val
        self.mstack.append(self.minval)
        
    def pop(self) -> None:
        self.stack.pop()
        self.mstack.pop()
        if self.mstack:
            self.minval = self.mstack[-1]
        else:
            self.minval = None

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.mstack[-1]    
