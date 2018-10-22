#Method 1:

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        s = s[::-1]
        
        return s

s = "A man, a plan, a canal: Panama"
Solution().reverseString(s):

#Method 2:

def reverseString(self, s):
    """
        :type s: str
        :rtype: str
        """
        S = list(s)
        
        i = 0;
        j = len(S) - 1
        while i < j :
            S[i], S[j] = S[j], S[i]
            i+=1
            j-=1
                            
        return ''.join(S)

s= "A man, a plan, a canal: Panama"
Solution().reverseString(s):
