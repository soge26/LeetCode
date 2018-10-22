#Method 1:

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        y=abs(x)
        z=[i for i in str(y)]
        z=z[::-1]
        a=int(''.join(z))
        
        if x<0:
            a*=-1
        
        if  a<-2**31 or a>2**31:
            return 0
        else:
            return a

x = 123
#x=-123
#x=1534236469
Solution().reverse(x)
