 #Method 1:

class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
    
        x = "{0:b}".format(num,fill="0")
        y=list(x)
        
        for v,i in enumerate(y):
            if int(i)>0:
                y[v]=int(i)-1
            else:
                y[v]=int(i)+1
        z = ''.join(list(map(str,y)))
        z = int(z, 2)
        return z

num = 5
num= 1
Solution().findComplement(num)
