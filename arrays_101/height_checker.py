# my solution
class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights)<1:
            return

        expected = heights[:]

        #sorting
        for i in range(len(expected) - 1):
            #print(expected)
            for j in range(i + 1, len(expected)):
                if expected[i] > expected[j]:
                    expected[i], expected[j] = expected[j], expected[i]

        #compare
        miss = 0
        for i in range(len(expected)):
            if expected[i]!=heights[i]:
                miss +=1
        return miss



heights = [1,1,4,2,1,3]
# Output: 3


# heights = [5,1,2,3,4]
# Output: 5


# heights = [1,2,3,4,5]
# Output: 0



print(Solution().heightChecker(heights))