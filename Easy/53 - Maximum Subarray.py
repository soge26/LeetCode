#Method 1:

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maxsum = 0
        
        
        for i in range(1,len(nums)):
            if nums[i-1]>0:
                nums[i]+=nums[i-1]


        #print(nums)
        return max(nums)

nums =[-2,1,-3,4,-1,2,1,-5,4]
Solution().maxSubArray(nums)
