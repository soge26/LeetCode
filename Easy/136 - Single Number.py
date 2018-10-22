#Method 1:

class Solution:
    def singleNumber(self, nums):
        """
            :type nums: List[int]
            :rtype: int
            """
        res = 0
        for num in nums:
            res ^= num
        
        #print(res)
        return res

nums = [2,2,1]
nums = [4,1,2,1,2]
Solution().singleNumber(nums)

#Method 2:

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashset = set()
            
            for i in nums:
                if i in hashset:
                    hashset.remove(i)
                else:
                    hashset.add(i)

        return (list(hashset)[0])

nums = [2,2,1]
nums = [4,1,2,1,2]
Solution().singleNumber(nums)
