#no memory used
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        if len(nums)<1:
            return

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == val:
                    nums[i], nums[j] = nums[j], nums[i]

        # while nums[::-1][0] == val:
        #     nums.pop()

        while nums:
            if len(nums)==0:
                break
            elif nums[::-1][0] != val:
                break
            nums.pop()

        #print(nums)



#
# nums = [3,2,2,3]
# val = 3
# Output: 2
# nums = [2,2,_,_]


nums = [0,1,2,2,3,0,4,2]
val = 2
# Output: 5
# nums = [0,1,4,0,3,_,_,_]



#
# nums = [1]
# val = 1
Solution().removeElement(nums,val)



# my two pointer solution


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        if len(nums) < 1:
            return

        pos = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
        return pos

#
# nums = [3,2,2,3]
# val = 3
# Output: 2
# nums = [2,2,_,_]


nums = [0,1,2,2,3,0,4,2]
val = 2
# Output: 5
# nums = [0,1,4,0,3,_,_,_]



#
# nums = [1]
# val = 1
print(Solution().removeElement(nums,val))


#fastest Solution
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        N = len(nums)
        l, r = 0, N - 1
        while l <= r:
            if nums[l] == val:
                nums[l] = nums[r]
                r -= 1
            else:
                l += 1
        return l




nums = [0,1,2,2,3,0,4,2]
val = 2



N = len(nums)
l,r=0,N-1

while l<=r:

    if nums[l]==val:
        nums[l]=nums[r]
        r-=1
    else:
        l+=1
