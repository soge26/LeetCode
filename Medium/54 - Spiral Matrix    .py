#Method 1: Recursive

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        if not matrix:
            return []
        bucket = []
        bucket += [matrix[0][0]]
        
        def right(matrix,i,j,count,bucket):
            #print(i,j,count,'right')
            k=1
            if count == rows*cols:
                return
            
            while True:
                try:
                    if(matrix[i][j+k])=='#':
                        down(matrix,i,j+k-1,count,bucket)
                        return
                    bucket+=[matrix[i][j+k]]
                    matrix[i][j+k]='#'
                    k+=1
                    count+=1
            
                except:
                    down(matrix,i,k-1,count,bucket)
                    return
            
            
        def down(matrix,i,j,count,bucket):
            #print(i,j,count,'down')
        
            k=1
            if count == rows*cols:
                return
            
            while True:
                try:
                    if(matrix[i+k][j])=='#':
                        left(matrix,i+k-1,j,count,bucket)
                        return
                    bucket+=[matrix[i+k][j]]
                    matrix[i+k][j]='#'
                    k+=1
                    count+=1
                except:
                    left(matrix,k-1,j,count,bucket)
                    return


        def left(matrix,i,j,count,bucket):
            #print(i,j,count,'left')
            k=1
            if count == rows*cols:
                return
                    
            while True:
                if(matrix[i][j-k])=='#':
                    up(matrix,i,j-k+1,count,bucket)
                    return
                if j-k<0:
                    up(matrix,i,0,count,bucket)
                    return
                bucket+=[matrix[i][j-k]]
                matrix[i][j-k]='#'
                k+=1
                count+=1
        
        def up(matrix,i,j,count,bucket):
            #print(i,j,count, 'up')
            k=1
            if count == rows*cols:
                return
            
            while True:
                
                if(matrix[i-k][j])=='#':
                    right(matrix,i-k+1,j,count,bucket)
                    return
                    count+=1
                    bucket+=[matrix[i-k][j]]
                    matrix[i-k][j]='#'
                    k+=1
            
        matrix[0][0]='#'
        rows= len(matrix)
        cols= len(matrix[0])
        count = 1
        right(matrix,0,0,count,bucket)
        return bucket

matrix = [
          [ 1, 2, 3],
          [ 4, 5, 6],
          [ 7, 8, 9],
          ]
matrix =[[1,2,3,4,5,6,7,8,9,10],
         [11,12,13,14,15,16,17,18,19,20],
         [21,22,23,24,25,26,27,28,29,30],
         [31,32,33,34,35,36,37,38,39,40],
         [41,42,43,44,45,46,47,48,49,50],
         [51,52,53,54,55,56,57,58,59,60],
         [61,62,63,64,65,66,67,68,69,70],
         [71,72,73,74,75,76,77,78,79,80],
         [81,82,83,84,85,86,87,88,89,90],
         [91,92,93,94,95,96,97,98,99,100]]
Solution().spiralOrder(matrix)

#Method 1: Iteratively

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        if not matrix:
            return []

        x = []
        y=matrix
        
        def printt(y,x):
            
            x+=list(y[0])
            y.remove(y[0])
            if not y:
                return x
            transpose(y,x)

        def transpose(y,x):
            y=list(zip(*y))[::-1]
            #print(matrix)
            printt(y,x)

        printt(matrix,x)
        return x

matrix = [
          [ 1, 2, 3],
          [ 4, 5, 6],
          [ 7, 8, 9],
          ]
matrix =[[1,2,3,4,5,6,7,8,9,10],
         [11,12,13,14,15,16,17,18,19,20],
         [21,22,23,24,25,26,27,28,29,30],
         [31,32,33,34,35,36,37,38,39,40],
         [41,42,43,44,45,46,47,48,49,50],
         [51,52,53,54,55,56,57,58,59,60],
         [61,62,63,64,65,66,67,68,69,70],
         [71,72,73,74,75,76,77,78,79,80],
         [81,82,83,84,85,86,87,88,89,90],
         [91,92,93,94,95,96,97,98,99,100]]
Solution().spiralOrder(matrix)


