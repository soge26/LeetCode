#Method 1:

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_count=0
        count=0
        for i in nums:
            if i!=0:
                count+=1
            else:
                count=0
            max_count= max(count,max_count)
            i+=1
        return max_count

nums=[1,1,0,1,1,1]
Solution().findMaxConsecutiveOnes(nums)
