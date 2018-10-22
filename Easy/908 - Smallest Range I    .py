#Method 1:

class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return max( (max(A)-K)-(min(A)+K), 0 )

A=[0,10]
K=2
#A=[1,3,6]
#K=3
#A=[2,7,2]
#K = 1
#A=[1]
#K=0
Solution().smallestRangeI(A, K)

#Method 2:

class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        
        A.sort()
        #print(A)
        max_A0= A[0]
        min_A = A[-1]
        min_diff = min_A-max_A0
            
        x=[max_A0+i for i in range(-1*K,K+1)]
        y=[min_A+i for i in range(-1*K,K+1)]
        #print(x)
        #print(y)
        
        for i in x:
            if i in y:
                return 0
            else:
                for j in y:
                    min_diff=min(min_diff,j-i)
        return min_diff

A=[0,10]
K=2
#A=[1,3,6]
#K=3
#A=[2,7,2]
#K = 1
#A=[1]
#K=0
Solution().smallestRangeI(A, K)

