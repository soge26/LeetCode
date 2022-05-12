# my solution
class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        if len(arr) < 3:
            #print (False)
            return False

        diff = -1
        i = 0

        if arr[0] - arr[1] > 0:
            #print(False)
            return False


        if arr[-1] - arr[-2] > 0:
            #print(False)
            return False

        while diff < 0 and i < len(arr) - 1:
            diff = arr[i] - arr[i + 1]
            if diff == 0:
                #print(False)
                return False
            i += 1

        while diff > 0 and i < len(arr) - 1:
            diff = arr[i] - arr[i + 1]
            if diff == 0:
                #print(False)
                return False
            elif diff < 0:
                #print(False)
                return False
            i += 1

        #print(True)
        return True



#
# arr = [2,1]
#
# arr = [3,5,5]


#arr = [0,3,2,1]

arr = [-2,-3,-2]

Solution().validMountainArray(arr)



# Fastest Solution


class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr)<3 or arr[1]<arr[0]: return False
        res = False
        clime = True
        up = False
        down = False
        i=1
        while i < len(arr) :
            if arr[i]==arr[i-1]: return False
            if clime:
                if arr[i]<arr[i-1]:
                    clime=False
            else:
                if arr[i]>arr[i-1]:
                    return False
            i+=1
        if clime: return False
        return True