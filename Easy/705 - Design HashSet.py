#Method 1:

class MyHashSet(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.map = [None]*self.size
    
    def get_hash(self,key):
        
        return key%self.size
    
    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        if self.contains(key):
            return
        
        key_hash = self.get_hash(key)
        if self.map[key_hash] is None:
            self.map[key_hash] = []
        self.map[key_hash] += [key]

    
    
    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        if not self.contains(key):
            return
    
        key_hash = self.get_hash(key)
        if self.map[key_hash] is not None:
            for i in self.map[key_hash]:
                if i == key:
                    self.map[key_hash].remove(i)



    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        key_hash = self.get_hash(key)
        if self.map[key_hash] is not None:
            if key in self.map[key_hash]:
                return True
                    
                    return False

obj = MyHashSet()
obj.add(key)
obj.remove(key)
param_3 = obj.contains(key)
