#Method 1:

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        x = (int(a,2))+(int(b,2))
        y = "{0:b}".format(x,fill="0")
        
        return y

a = "11"
b = "1"
a = "1010"
b = "1011"
Solution().addBinary(a, b)


