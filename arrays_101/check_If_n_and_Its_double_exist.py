# my solution
class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        if len(arr)<0:
            return

        doubles = {}

        for i in arr:
            if doubles.get(2*i,False)!=False:
                print(2*i,i)
                return True
            elif doubles.get(.5*i,False)!=False:
                print(int(.5 * i), i)
                return True
            else:
                doubles[i] = True
        print(doubles)
        return False


#arr = [10,2,5,3]

#arr = [7,1,14,11]
#
arr = [3,1,7,11]

Solution().checkIfExist(arr)


# fastest solutoin

class Solution(object):
    def checkIfExist(self, arr):
        for i in arr:
            if i == 0 and arr.count(i) > 1:
                return True
            elif i == 0 and arr.count(i) == 1:
                pass
            elif i*2 in arr:
                return True
        return False