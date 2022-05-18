class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        return nums*2
        #return nums+nums

nums = [1,2,1]
print(Solution().getConcatenation(nums))