#Method 1:

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        temp = [None]*len(A)
        odd=1
        even=0
        for v,i in enumerate(A):
            if i%2==0:
                temp[even]=i
                even+=2
            else:
                temp[odd] = i
                odd+=2
        
        return temp

A=[4,2,5,7]
Solution().sortArrayByParityII(A)
