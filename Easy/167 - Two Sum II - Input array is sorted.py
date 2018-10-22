#Method 1:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        bucket= {}
        
        for v,i in enumerate(numbers):
            
            if i in bucket:
                return bucket[i]+1,v+1
            else:
                bucket[target-i]=v

numbers = [2,7,11,15]
target = 9
Solution().twoSum(numbers, target)
