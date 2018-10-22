#Method 1:

class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        temp1 = [None]*len(S)
        temp2 = []
        
        for v,i in enumerate(S):
            if ord(i)<65 or 90<ord(i)<97:
                temp1[v]= i
            else:
                temp2.append(i)
        
        s = temp2[::-1]
        i = v = 0
        
        while i<len(s):
            #print(temp1)
            if not temp1[v]:
                temp1[v]=s[i]
                i+=1
                v+=1
            else:
                v+=1
    
        return ''.join(temp1)

S= "a-bC-dEf-ghIj"
Solution().reverseOnlyLetters(S)

