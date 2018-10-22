#Method 1:

class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        x="{0:b}".format(n)
        y=list(map(int,x))
        last=0
        
        for i in y:
            if i==last:
                return False
            last=i
        return True
x=10
#x=11
Solution().hasAlternatingBits(x)
