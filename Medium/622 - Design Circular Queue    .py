#Method 1:

class MyCircularQueue(object):
    
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.cap = k
        self.queue= [None]*k
        self.f = 0
        self.r = k-1
    
    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.r = (self.r+1) % self.cap
        self.queue[self.r]=value
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.queue[self.f]=None
        self.f = (self.f+1) % self.cap
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
            
        if self.isEmpty():
            return -1
        return self.queue[self.f]


    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[self.r]


    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        if self.f ==  ((self.r + 1) % self.cap) and self.queue[self.f] is None:
            return True
        return False


    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        if self.f ==  ((self.r + 1) % self.cap) and self.queue[self.f] is not None:
            return True
        return False




obj = MyCircularQueue(k)
param_1 = obj.enQueue(value)
param_2 = obj.deQueue()
param_3 = obj.Front()
param_4 = obj.Rear()
param_5 = obj.isEmpty()
param_6 = obj.isFull()
