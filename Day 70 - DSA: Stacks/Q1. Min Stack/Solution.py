class MinStack:        
    
    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack.append(x)
        if not self.min_stack:
            self.min_stack.append(x)
        else:
            self.min_stack.append(min(x, self.min_stack[-1]))
        

    # @return nothing
    def pop(self):
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
        

    # @return an integer
    def top(self):
        if not self.stack:
            return -1
        return self.stack[-1]
        

    # @return an integer
    def getMin(self):
        if not self.min_stack:
            return -1
        return self.min_stack[-1]
        
    
    def __init__(self):
        self.stack = []
        self.min_stack = []