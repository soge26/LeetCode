#Method 1:

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        i=0
        while i <len(nums)-1:
            
            
            if nums[i]==nums[i+1]:
                nums.remove(nums[i])
                i+=0
            else:
                i+=1
    
        return len(nums)

nums = [1,1,2]
Solution().removeDuplicates(nums)

#Method 2:

class Solution:
    def removeDuplicates(self, nums):
        """
            :type nums: List[int]
            :rtype: int
            """
        x = len(nums)
        if x == 0:
            return 0
        elif x == 1:
            return(1)
        else:
            i=0
            while i <len(nums)-1:
                
                if nums[i]==nums[i+1]:
                    nums.remove(nums[i])
                    i+=0
                else:
                    i+=1

        return len(nums)

nums = [1,1,2]
Solution().removeDuplicates(nums)
