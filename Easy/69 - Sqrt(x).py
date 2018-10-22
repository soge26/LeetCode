#Method 1:

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        import math        
        return math.floor(x**0.5)

x= 16
Solution().mySqrt(x)

