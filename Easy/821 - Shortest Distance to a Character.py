#Method 1:

class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        
        if C not in S:
            return 0
        
        s=list(S)
        x=[]
        z=[0]*len(s)
        for v,i in enumerate(s):
            if i ==C:
                x.append(v)
        
        #print(z)
        #print(x)
            
        for i in range(len(s)):
            y = [abs(i-t) for t in x]
            z[i]+= min(y)        
        
        return z

S = "loveleetcode"
C = 'e'
Solution().shortestToChar(S, C)
