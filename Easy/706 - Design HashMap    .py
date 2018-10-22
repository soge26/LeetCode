#Method 1:

class MyHashMap(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.map = [None]*self.size
    
    def get_hash(self,key):
        
        return key%self.size
    
    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        key_hash = self.get_hash(key)
        key_value = [key,value]
        if self.map[key_hash] is None:
            self.map[key_hash] =[]
            self.map[key_hash].append(key_value)
            return True
        else:
            for i in self.map[key_hash]:
                if i[0]==key:
                    i[1]=value
                    return
            self.map[key_hash].append(key_value)
            return True



    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        key_hash = self.get_hash(key)
        if self.map[key_hash] is not None:
            for i in self.map[key_hash]:
                if i[0] == key:
                    if len(i) ==1:
                        return -1
                    return i[1]
            return -1
        else:
            return -1


    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        key_hash = self.get_hash(key)
        if self.map[key_hash] is not None:
            for i in self.map[key_hash]:
                if i[0] == key:
                    self.map[key_hash].remove(i)

obj = MyHashMap()
obj.put(key,value)
param_2 = obj.get(key)
obj.remove(key)
