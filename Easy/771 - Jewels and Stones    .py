#Method 1:

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        
        y=[]
        for i in J:
            x=S.count(i)
            y.append(x)
        
        return sum(y)

J = "aA"
S = "aAAbbbb"
#J = "z"
#S = "ZZ"
Solution().numJewelsInStones(J, S)

#Method 2:

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count =0
        for i in S:
            if i in J:
                count += 1
        return count

J = "aA"
S = "aAAbbbb"
#J = "z"
#S = "ZZ"
Solution().numJewelsInStones(J, S)
