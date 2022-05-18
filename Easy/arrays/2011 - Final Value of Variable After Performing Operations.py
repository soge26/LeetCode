# my solution

class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """

        for i in range(len(operations)):
            if (operations[i] =="--X") | (operations[i] == "X--"):
                operations[i]=-1
            else:
                operations[i] = 1

        return sum(operations)


operations = ["--X","X++","X++"]

print(Solution().finalValueAfterOperations(operations))



# fastest solution


class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        r=0
        for i in operations:
            if i[1] == "+":r+=1
            else:r-=1
        return r

