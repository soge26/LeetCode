#Method 1:

class Solution:
    def isPowerOfFour(self, n):
        """
            :type num: int
            :rtype: bool
            """
        x = 4
        if n == 0 :
            return False
        
        if n == 1:
            return True
        
        elif 0<n<1:
            while x > n:
                
                x= x/4
        
        else:
            while x < n:
                
                x= x*4
        
        if x == n:
            return True
        else:
            return False

n = 8
n = 16
Solution().isPowerOfFour(n):

