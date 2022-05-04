# my solution
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        if len(nums)==0:
            return

        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
        #print (nums)

nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]


#nums = [0]
# Output: [0]

Solution().moveZeroes(nums)


# fastest solution
class Solution(object):
    def moveZeroes(self, nums):
        zero=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i], nums[zero]=nums[zero], nums[i]
                zero+=1