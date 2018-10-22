#Method 1:

class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        x = 2
        
        if n == 0 :
            return False
        if n == 1:
            return True
        elif 0<n<1:
            while x > n:
                x= x/2
        else:
            while x < n:
                x= x*2
            
        if x == n:
            return True
                else:
            return False
y=10
#y=32
#y=128
#y=1024
Solution().isPowerOfTwo(y):
