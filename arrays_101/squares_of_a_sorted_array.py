# my solution

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        array = [None] * len(nums)

        for i, v in enumerate(nums):
            array[i] = v * v

        return sorted(array)



# most popular solution


class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        nums.sort()
        return nums


# best solution


class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        for i in nums:
            arr.append(i * i)

        return sorted(arr)
