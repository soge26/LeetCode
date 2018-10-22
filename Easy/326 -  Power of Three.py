#Method 1:

class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x = 3
        if n == 0 :
            return False
        
        if n == 1:
            return True
        
        elif 0<n<1:
            while x > n:
                
                x= x/3
        
        else:
            while x < n:
                
                x= x*3
        print(x)
        if x == n:
            return True
        else:
            return False

n = 6
n = 27
Solution().isPowerOfThree(n):

