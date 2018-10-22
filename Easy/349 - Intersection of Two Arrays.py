#Method 1:

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        hashset = set()
        
        for i in nums1:
            hashset.add(i)
        
        for j in list(hashset):
            if j not in nums2:
                hashset.remove(j)
        
        return list(hashset)

nums1=[1,2,2,1]
nums2=[2,2]
Solution().intersection(nums1, nums2):
