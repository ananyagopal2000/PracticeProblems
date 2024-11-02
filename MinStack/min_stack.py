"""
MinStack_I: 
Push value into stack - append value into stack and minimum value into min-stack when minimum value is found
Pop value into stack - pop from min-stack only when the popped elemen from the main stack is equal to the top element in min-stack

MinStack_II: to handle duplicates and multiple min value
Push value into stack - append value into stack and minimum value into min-stack, finally: len(stack)=len(min-stack)
Pop value into stack - pop both stack and min-stack
so to get the min value at any point we have to pop the min_stack.
"""
class MinStack:
    def __init__(self):
        self.stack=[]
        self.min_stack=[]
    
    def push(self, val):
        self.stack.append(val)

        if self.min_stack:
            val=min(val, self.min_stack[-1])

        if val not in self.min_stack:
            self.min_stack.append(val)

            
    def pop(self):
        popped=self.stack.pop(-1)  

        if popped==self.min_stack[-1]:        
            self.min_stack.pop(-1)

        return self.stack
    
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.min_stack[-1]


class MinStack_II:
    def __init__(self):
        self.stack=[]
        self.min_stack=[]
    
    def push(self, val):
        self.stack.append(val)
        if self.min_stack:
            val=min(val, self.min_stack[-1])

        self.min_stack.append(val)
        return self.stack
    
    def pop(self):
        self.stack.pop(-1)  
        self.min_stack.pop(-1)
        return self.stack
    
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.min_stack[-1]
# make min_stack smaller
# support duplicate elements also eg: [1,2,3,-1,2,1,2] 