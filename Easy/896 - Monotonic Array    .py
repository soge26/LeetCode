#Method 1:

class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        
        AI= sorted(A)
        AD= AI[::-1]
        
        return  A==AI or A==AD

A= [1,2,2,3]
#A = [3,2,2,1]
Solution().isMonotonic(A)
