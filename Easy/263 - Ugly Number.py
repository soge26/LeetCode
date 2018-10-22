#Method 1:

class Solution:
    def isUgly(self, num):
        """
            :type num: int
            :rtype: bool
            """
        
        ugly = [2,3,5]
        
        if num==0:
            return False
        
        if num in ugly:
            return True
        
        while num%2==0:
            num= num/2
        
        while num%3==0:
            num= num/3
        
        while num%5==0:
            num= num/5
        
        
        if num==1:
            return True
        else:
            return False

x=7
#x=24
#x=720
Solution().isUgly(num):
