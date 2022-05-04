# my solution
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1. Declare starting position
        # 2. Find the next non duplicate value index
        # 3. Change the next array index value to the next non duplicate value


        if len(nums)==0:
            return 0

        pos = 0

        for i in range(1,len(nums)):
            #print(i)
            if nums[i]!=nums[i-1]:
                nums[pos+1]=nums[i]
                pos+=1

        return pos+1

#nums = [1,1,2]
# Output: 2
# nums = [1,2,_]
#
#
nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5
# nums = [0,1,2,3,4,_,_,_,_,_]

#nums=[1,1]
Solution().removeDuplicates(nums)



# fastest solution


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums) == 0):
            return 0
        i = 0
        for j in range(1, len(nums)):
            if (nums[j] != nums[i]):
                i += 1
                nums[i] = nums[j]

        return i + 1