#Method 1:

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        from collections import Counter
        
        nums = sorted(nums)
        c = Counter(nums)
        c1 = list(c.values())
        c2 = list(c.keys())
        clists = list(zip(c1, c2))
        clists.sort()
        p= list(zip(*clists))[1]
        return sorted(list(p[-k::]))

nums = [3,3,3,1,1,1,2,2,3]
#nums = [1,2]
#nums=[1,1,1,2,2,3]
#nums = [4,1,-1,2,-1,2,3]
k = 2
Solution().topKFrequent(nums, k)
