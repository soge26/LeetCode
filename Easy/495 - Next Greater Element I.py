#Method 1:

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        y=[]
        for i in nums1:
            x = nums2.index(i)
            
            if i == nums2[-1]:
                y+=[-1]
            
            elif max(nums2[x+1::])>i:
                for j in nums2[x+1::]:
                    if j>i:
                        y+=[j]
                        break
            else:
                y+=[-1]
        return y

nums1 = [4,1,2]
nums2 = [1,3,4,2]
#nums1 = [2,4]
#nums2 = [1,2,3,4]
#nums1=[1,3,5,2,4]
#nums2=[6,5,4,3,2,1,7]
Solution().nextGreaterElement(nums1, nums2)

