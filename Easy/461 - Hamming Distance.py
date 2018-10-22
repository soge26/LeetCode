 #Method 1:

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        x1="{0:{fill}32b}".format(x,fill='0')
        y1="{0:{fill}32b}".format(y,fill='0')
        print(x1)
        print(y1)
        count =0
        for i,j in zip(x1,y1):
            if i!=j:
                count+=1
        return count
x = 1
y = 4
#x=680142203
#y=1111953568

Solution().hammingDistance(x, y)
