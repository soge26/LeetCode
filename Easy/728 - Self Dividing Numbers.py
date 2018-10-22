#Method 1:

class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        
        x=0
        y=[]
        z= []
        for i in range(left, right+1):
            
            if '0' in str(i):
                continue
            else:
                y= [x+1 for j in str(i) if i%int(j)==0]
            if sum(y)==len(str(i)):
                z+=[i]
        return z

left = 3339
right = 3341
Solution().selfDividingNumbers(left, right)
