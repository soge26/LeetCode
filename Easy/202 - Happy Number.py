#Method 1:

class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def happy(t):
            
            x = list(map(int, str(t)))
            y=0
            
            for i in x:
                y+= i**2
            
            return y
        
        result = happy(n)
        path = []
        while True:
            #print(result,path)
            path.append(result)
            
            
            if result!=1:
                result = happy(result)
            
            else:
                return True
            #print(result,path)
            
            if result in path:
                return False

n= 19
n= 19
#n= 82
#n= 68
#n= 10
Solution().isHappy(n)
