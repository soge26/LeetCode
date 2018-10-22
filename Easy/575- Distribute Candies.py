#Method 1:

class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        
        return int(min(len(candies)/2,len(set(candies))))

candies = [1,1,2,2,3,3]
#candies = [1,1,2,3]
#candies = [1,11]
#candies = [1,1,1,100]
#candies =[1000,1000,2,1,2,5,3,1]
Solution().distributeCandies(candies)
