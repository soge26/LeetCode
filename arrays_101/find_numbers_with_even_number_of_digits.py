# my solution


class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        amt = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                amt += 1

        return amt


Solution().findNumbers([555,901,482,1771])
