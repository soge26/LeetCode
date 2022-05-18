class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # 2 pointer method
        pos = 0
        i=0

        # counter
        c=0


        n = len(nums)

        # while i != pos if i nums[i] is less than nums[pos] increase counter
        while pos < n:
            if i == n:
                nums.append(c)
                c=0 # reset counter
                pos += 1
                i = 0 # reset i
            if pos==n:
                break
            if nums[pos] > nums[i] and pos != i:
                c += 1
            i += 1
        return nums[n:]


nums = [8,1,2,2,3]
nums = [6,5,4,8]
nums = [7,7,7,7]

print(Solution().smallerNumbersThanCurrent(nums))


# fastest solution

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nums_copy = nums[:]
        nums.sort()
        # sorting of nums
        # [1, 2, 2, 3, 8]
        appearances = {nums[0]: 0}
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                appearances[nums[i]] = i

            # population of appearances
            # {1: 0, 2: 1}
            # {1: 0, 2: 1}
            # {1: 0, 2: 1, 3: 3}
            # {1: 0, 2: 1, 3: 3, 8: 4}
        return_arr = []
        for num in nums_copy:
            return_arr.append(appearances[num])
        return return_arr
