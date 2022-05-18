# my solution
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        pos = 0
        i=1
        c = 0
        if len(nums)<2:
            return
        while pos < len(nums)-2:
            # print('pos:', pos)
            # print('i:', i)
            # print('c:',c)
            if i==len(nums):
                pos+=1
                i=pos+1
            if nums[pos] == nums[i]:
                c+=1
            i+=1
        return c

from itertools import combinations


nums = [1,2,3,1,1,3]
nums = [1,1,1,1]
nums = [1,2,3]

print(Solution().numIdenticalPairs(nums))


# fastest solution


class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=0
        pairs ={}
        for i in nums:
            if i in pairs:
                pairs[i]+=1
            else:
                pairs[i]=1
        for i in pairs:
            result+= pairs[i]*(pairs[i]-1)/2
        return int(result)