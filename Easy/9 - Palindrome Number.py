#Method 1:

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        y= list(str(x))
        
        y=y[::-1]
        
        z=''.join(y)
        
        if z==str(x):
            return True
        else:
            return False


x=-121
x=121
Solution().isPalindrome(x)
