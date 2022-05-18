# my solution
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        most = max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies >= most:
                candies[i]=True
            else:
                candies[i]=False
        return candies

candies = [2,3,5,1,3]
extraCandies = 3

candies = [4,2,1,1,2]
extraCandies = 1

candies = [12,1,12]
extraCandies = 10
print(Solution().kidsWithCandies(candies,extraCandies))

# fastest solution
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        l = len(candies)
        most = max(candies)
        # boo = [False]*l

        for i in range(l):
            if (candies[i] + extraCandies) >= most:
                candies[i] = True
            else:
                candies[i] = False

        return candies