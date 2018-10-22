#Method 1:

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for v,i in enumerate(nums):
            if count==sum(nums[v+1::]):
                return(v)
            count+=i
        return -1

nums =[1, 7, 3, 6, 5, 6]
Solution().pivotIndex(nums)

#Method 2:

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = sum(nums)
        for v,i in enumerate(nums):
            right-=i
            if left==right:
                return(v)
            left+=i
        return -1

nums =[1, 7, 3, 6, 5, 6]
Solution().pivotIndex(nums)

#Method 3:

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left = 0
        right = sum(nums)
        for v,i in enumerate(nums):
            right-=i
            if left==right:
                return(v)
            left+=i
        return -1

nums =[1, 7, 3, 6, 5, 6]
Solution().pivotIndex(nums)
