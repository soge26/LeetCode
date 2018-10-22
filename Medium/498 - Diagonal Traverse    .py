#Method 1:

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        from collections import defaultdict
        if not matrix:
            return []
        traversal = []
        bucket = defaultdict(list)
        rows = len(matrix)
        cols = len(matrix[0])
        
        for i in range(rows):
            for j in range(cols):
                sum_=i+j
                bucket[sum_].append(matrix[i][j])
        for i in bucket:
            if i%2==0:
                traversal+=bucket[i][::-1]
            else:
                traversal+=bucket[i]
        return traversal

matrix = [
          [ 1, 2, 3 ],
          [ 4, 5, 6 ],
          [ 7, 8, 9 ]
          ]
matrix = [
          [ 1, 2, 3, 4 ],
          [ 5, 6, 7, 8 ],
          [ 9, 10, 11, 12 ]
          ]
matrix = [
          [ 1, 2, 3 ],
          [ 4, 5, 6 ],
          [ 7, 8, 9 ],
          [10, 11, 12 ]
          ]

matrix = [ [ 1, 2, 3 ] ]
matrix = [ [ 1], [2], [3 ] ]
matrix = [ [ ] ]
matrix = [ [ 1,2], [4, 3 ] ]
matrix =[[2,5],[8,4],[0,-1]]
matrix =[[2,5,8],[4,0,-1]]
matrix=[[1,2,3,4,5,6,7,8,9,10]]
matrix=[[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]

Solution().findDiagonalOrder(matrix)


