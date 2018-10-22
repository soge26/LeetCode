#Method 1:

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == []:
            return False
        s = set(nums)
        for i in s:
            if nums.count(i)>1:
                return True
        return False

nums = [1,2,3,1]
#nums=[2,14,18,22,22]
Solution().containsDuplicate(nums)

#Method 2:

containsDuplicate(nums)
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == []:
            return False
        
        from collections import Counter
        
        c = Counter(nums)
        c = list(c.values())
        
        s = sum(c)/(len(c))
                return s!=1

nums = [1,2,3,1]
#nums=[2,14,18,22,22]
Solution().containsDuplicate(nums)

#Method 3:

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        hashset = set()
        
        for i in nums:            
            if i in hashset:
                return True
            hashset.add(i)
        
        return False

nums = [1,2,3,1]
#nums=[2,14,18,22,22]
Solution().containsDuplicate(nums)
