#Method 1:

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        r = sum(nums)
        s = sum(range(len(nums)+1))
        
        return s-r

nums = [9,6,4,2,3,5,7,0,1]
#nums=[0]
#nums= [0,1]
Solution().missingNumber(nums)
