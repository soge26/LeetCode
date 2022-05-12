# my solution

class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i=0
        j = len(arr) - 1

        while i<len(arr):
            if arr[i]==0:
                while j > i:
                    arr[j]=arr[j-1]
                    j-=1
                j = len(arr) - 1
                i+=1

            #print (arr)
            #print (i)
            i+=1


Solution().duplicateZeros([1,0,2,3,0,4,5,0])
#arr = [1,0,2,3,0,4,5,0]



# most popular solution

class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        self.arr = arr
        l = len(self.arr)
        print("L1", l)
        idx = 0
        while idx < l:
            if self.arr[idx] == 0:
                print(self.arr[idx])
                self.arr.insert(idx + 1, 0)
                idx += 2
                self.arr.pop()
            else:
                idx += 1


# fastest solution

class Solution(object):
    def duplicateZeros(self, arr):
        zeros = 0
        length = len(arr) - 1
        for left in range(length + 1):
            if left + zeros > length:
                break

            if arr[left] == 0:
                if left + zeros == length:
                    arr[length] = 0
                    length -= 1
                    break
                zeros += 1

        last = length - zeros
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + zeros] = 0
                zeros -= 1
                arr[i + zeros] = 0
            else:
                arr[i + zeros] = arr[i]