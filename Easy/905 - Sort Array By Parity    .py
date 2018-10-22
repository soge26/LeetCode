#Method 1:

class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        j=0
        
        for v,i in enumerate(A):
            
            if i%2==0:
                A[j], A[v]=A[v], A[j]
                j+=1
    
        return A

A= [3,1,2,4]
Solution().sortArrayByParity(A)
