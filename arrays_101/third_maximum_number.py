class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #1. sorted in reverse
        #2. removed duplicates

        if len(nums) == 0:
            return
        if len(nums) == 1:
            return nums[0]

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]

        pos = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[pos]:
                nums[pos + 1] = nums[i]
                pos += 1

        if pos+1 < 3:
            return max(nums[:pos+1])
        else:
            return nums[2]





# nums = [3,2,1]

#nums = [1,2]

# nums = [2,2,3,1,4]

# nums = [0]
# nums = [1,2,2,5,3,5]

# print(Solution().thirdMax(nums))

# print([2, 3, 1, 4, 4][:3])



#fastest solution

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Max1=None
        Max2=None
        Max3=None
        for i in nums:
            if not Max1 or i > Max1:
                Max3=Max2
                Max2=Max1
                Max1=i
            elif i == Max1:
                continue
            elif not Max2 or i > Max2:
                Max3=Max2
                Max2=i
            elif i == Max2:
                continue
            elif not Max3 or i > Max3:
                Max3=i
        if Max3 != None :
            return Max3
        else:
            return Max1


# my second solution
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums2 =  [None]*3
        max = 0
        for i in range(len(nums)):
            if not nums2[0] or nums[i] > nums2[0]:
                nums2[0], nums2[1], nums2[2] = nums[i], nums2[0], nums2[1]
                print(nums2)
            elif not nums2[1] or nums[i]>nums2[1]:
                if nums[i] != nums2[0]:
                    nums2[1], nums2[2] = nums[i], nums2[1]
            elif not nums2[2] or nums[i]> nums2[2]:
                if nums[i] != nums2[1]:
                    nums2[2]=nums[i]
        print(nums2)

        if nums2[2]!=None:
            return nums2[2]
        else:
            return nums2[0]


# nums = [3,2,1]

# nums = [1,2]

# nums = [2,2,3,1,4]
# nums = [2,2,3,1]
nums = [3,3,4,3,4,3,0,3,3]
# nums = [0]
# nums = [1,2,2,5,3,5]

print(Solution().thirdMax(nums))



# solution using builtin functions

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        list_1 = sorted(list(set(nums)))
        if len(list_1) >= 3:
            return list_1[-3]
        else:
            return list_1[-1]


# solution using hashset


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        hashset = set(nums)

        if len(hashset) < 3:
            return max(hashset)

        first_high = max(hashset)
        hashset.remove(first_high)

        second_high = max(hashset)
        hashset.remove(second_high)

        return max(hashset)