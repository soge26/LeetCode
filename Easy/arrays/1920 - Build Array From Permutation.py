# my solution
class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums2 = [None] * (len(nums))

        for i in range(len(nums)):
            nums2[i] = nums[nums[i]]

        return nums2


nums = [1,0]

Solution().buildArray(nums)


# one-liner

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]


# fastest solution
class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        for i in range(len(nums)):
            output.append(nums[nums[i]])
        return output