# my solution
class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """

        max = 0
        for i in accounts:
            if sum(i) > max:
                max = sum(i)
        return max

accounts = [[1,2,3],[3,2,1]]
accounts = [[1,5],[7,3],[3,5]]

print(Solution().maximumWealth(accounts))


# fastest solution

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        wealth = []
        for account in accounts:
            wealth.append(sum(account))
        return max(wealth)