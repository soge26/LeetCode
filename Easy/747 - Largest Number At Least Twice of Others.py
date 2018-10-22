#Method 1:

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums)==1:
            return 0
        
        x=sorted(nums,reverse=True)
        
        if x[0]>=x[1]*2:
            return nums.index(x[0])
        return -1

nums = [0,0,0,1]
#nums = [3, 6, 1, 0]
Solution().dominantIndex(nums)
