#Method 1:

class Solution(object):
    
    def twoSum(self, nums, target):
        #type nums: List[int]
        #type target: int
        #rtype: List[int]
        i = 0

        while i <= len(nums)-1:
            x = (target-nums[i])
            #print(x)

            #if x==nums[i]:
            #    i+=1
            if x in nums and nums.index(x) != i:

                return sorted([i,nums.index(x)])
            else:
                i+=1

numbers = [2,7,11,15]
target = 9
Solution().twoSum(numbers, target)

#Method 2:

class Solution(object):
 
	def twoSum(self, nums, target):
        #type nums: List[int]
        #type target: int
        #rtype: List[int]

        hashmap = {}

   		for v,i in enumerate(nums):

        		if target-i in hashmap:
            		return hashmap[target-i],v 
        		hashmap[i]=v

numbers = [2,7,11,15]
target = 9
Solution().twoSum(numbers, target)
