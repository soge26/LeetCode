#Method 1:

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        from math import factorial
        def combination(i,j):
            x=factorial(i)
            y= factorial(i-j)*factorial(j)
            z=x/y
            return int(z)
        
        
        bucket = []
        
        for i in range(numRows):
            bucket.append([combination(i,j) for j in range(i+1)])
        
        return bucket

Solution().generate(100)


#Method 2:


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        from sympy import binomial
        
        bucket = []
        
        for i in range(numRows):
            bucket.append([binomial(i,j) for j in range(i+1)])
            return bucket

Solution().generate(6)
