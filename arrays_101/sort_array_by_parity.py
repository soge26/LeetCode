# my solution
class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if len(nums)==0:
            return

        pos = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
        return nums

nums = [3,1,2,4]
# Output: [2,4,3,1]


# fastest solution
class Solution(object):
    def sortArrayByParity(self, nums):
        nums.sort(key = lambda y: y % 2)
        return nums



Solution().sortArrayByParity(nums)
