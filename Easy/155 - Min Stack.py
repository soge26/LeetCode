#Method 1:

class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
    
    
    
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack1.append(x)
    
    
    
    def pop(self):
        """
        :rtype: void
        """
        self.stack1.pop()
    
    
    def top(self):
        """
        :rtype: int
        """
        if len(self.stack1)==0:
            return -1
        if len(self.stack1)==1:
            return self.stack1[0]
        return self.stack1[-1]
    
    
    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack1)==0:
            return -1
        if len(self.stack1)==1:
            return self.stack1[0]
        return min(self.stack1)

obj = MinStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
