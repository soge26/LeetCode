class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        max = 0

        if len(arr) < 0:
            return

        if len(arr) == 1:
            arr[0] = -1
            return arr

        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                if arr[j] > max:
                    max = arr[j]
            arr[i] = max
            max = 0
        arr[-1] = -1
        return arr



arr = [17,18,5,4,6,1]

#arr = [400]

print(Solution().replaceElements(arr))

#fast solution

class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        if not arr:
            return []
        if len(arr) == 1:
            return [-1]

        maxElm = arr[-1]
        arr[-1] = -1
        for i in range(len(arr) - 2, -1, -1):
            temp = arr[i]
            arr[i] = maxElm
            maxElm = max(maxElm, temp)
        return arr