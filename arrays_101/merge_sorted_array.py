
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # first combines items of nums1 and nums2 then sorts the array.

        if n==0:
            return

        total = nums1[:m] + nums2

        for i in range(len(total)):
            for j in range(i+1,len(total)):
                if total[i]>total[j]:
                    total[i],total[j]=total[j],total[i]

            nums1[i]=total[i]
        #print(nums1)
#test1
# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3

#test2
# nums1 = [1]
# m = 1
# nums2 = []
# n = 0


#test3
# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1


# nums1 = [4,5,6,0,0,0]
# m = 3
# nums2 = [1,2,3]
# n = 3


# nums1=[-1,0,0,3,3,3,0,0,0]
# m = 6
# nums2 = [1,2,2]
# n = 3


nums1= [1,0]
m = 1
nums2 = [2]
n = 1


Solution().merge(nums1,m,nums2,n)



# fastest solution


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # compare the largest numbers (nums1 vs nums2)
        # if nums1[i] >= nums2[j] => add nums1[i] to the end of the list
        # else => add nums2[j] to the end
        # check if i or j reaches -1 first (all values of that sub-list had been added to nums1)
        # if i reaches 0 first and there are still some items in j not yet added
        # replace un-updated nums in nums1 with remaining ones in nums2

        i = m - 1
        j = n - 1

        current_index = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[current_index] = nums1[i]
                i -= 1
            else:
                nums1[current_index] = nums2[j]
                j -= 1
            current_index -= 1

        if j >= 0:
            nums1[:current_index + 1] = nums2[:j + 1]

        return nums1