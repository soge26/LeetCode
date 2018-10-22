#Method 1:

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        x = nums.count(0)
        y = [0]*x
        
        for i in range(x):
            nums.remove(0)
        
        nums.extend(y)

nums = [0,1,0,3,12]
Solution().moveZeroes(nums)

