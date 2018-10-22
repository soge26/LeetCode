#Method 1:

class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        
        x = list(zip(*A))
        y = [list(i) for i in x]
        return y

A = [[1,2,3],[4,5,6],[7,8,9]]
A = [[1,2,3],[4,5,6]]
Solution().transpose(A)
