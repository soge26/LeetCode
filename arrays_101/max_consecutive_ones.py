
# my solution
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        maxcount = 0

        for i in nums:
            if i == 1:
                count += 1
            else:
                count = 0

            if count > maxcount:
                maxcount = count

        return maxcount


# best solution


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        cnt = 0
        ans = 0
        for num in nums:
            if num == 1:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 0
        return ans