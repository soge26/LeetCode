#Method 1:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        max_num = 0
        for i in s:
            if nums.count(i)>max_num:
                max_num = nums.count(i)
                x = i
        return x

nums= [3,2,3]
nums= [2,2,1,1,1,2,2]
Solution().majorityElement(nums)
