#Method 1:

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        i=0
        x=0
        while i<=len(nums):
            try:
                x+= min(nums[i:i+2])
                i+=2
            except:
                break
        return x

nums = [1,4,3,2]
Solution().arrayPairSum(nums)


