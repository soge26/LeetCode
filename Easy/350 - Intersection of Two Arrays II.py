#Method 1:

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        
        
        n1 = defaultdict(int)
        
        for i in nums1:
            n1[i]+=1
    
        n2 = defaultdict(int)
        
        for i in nums2:
            n2[i]+=1

        x = []

        for key in n1:
            if key in n2:
                s = [key]*min(n1[key],n2[key])
                x.extend(s)
        return x

nums1 = [1,2,2,1]
nums2 = [2,2]
#nums1 = [4,9,5]
#nums2 = [9,4,9,8,4]
Solution().intersect(nums1, nums2)
