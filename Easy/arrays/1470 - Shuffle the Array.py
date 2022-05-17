#my solution
class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """

        x = nums[:n]
        y = nums[n:]
        c=0
        d=0
        for i in range(len(nums)-1):
            if i%2==0:
                nums[i] = x[c]
                c += 1
            else:
                nums[i] = y[d]
                d+=1
        return nums



#fastest solution
class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        for i in range(n):
            nums.append(nums[i])
            nums.append(nums[n +i])
         # since n is half the array, n *2 is the full array
		 # we append new values to the array
		 # and return the second half as the result
        return nums[n*2::]




nums = [2,5,1,3,4,7]
n = 3

nums = [1,2,3,4,4,3,2,1]
n = 4

nums = [1,1,2,2]
n = 2

nums = [1,0]
n = 2

print(Solution().shuffle(nums,n))