#Method 1:

class Solution:
    def checkPossibility(self, nums):
        """
            :type nums: List[int]
            :rtype: bool
            """
        i=0
        count=0
        
        while i in range(0,len(nums)):
            #print(nums)
            if count>=2:
                break
            try:
                if nums[i+1]< nums[i]:
                    count +=1
                    if nums[i+2]>=nums[i]:
                        nums[i+1]=nums[i+2]
                
                    elif nums[i+2]<=nums[i]:
                        nums[i]=nums[i+1]
                    i=0
            else:
                i+=1
            except:
                break
        return count<2

nums=[4,2,3]
#nums=[4,2,1]
#nums=[4,3,2]
#nums=[3,4,2,3]
#nums=[2,3,3,2,4]
#nums=[1,3,2,3,3]
Solution().checkPossibility(nums)
