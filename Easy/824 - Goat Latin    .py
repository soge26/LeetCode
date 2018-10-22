#Method 1:

class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        s=S.split(' ')
        vowels = ['a','e','i','o','u']
        x='ma'
        y=[]
        
        for v,i in enumerate(s):
            
            if i[0].lower() in vowels:
                y+=[i+x+('a'*(v+1))]
            else:
                y+=[i[1::]+i[0]+x+('a'*(v+1))]
        
        z= ' '.join(y)
        return z

S= "I speak Goat Latin"
S= "The quick brown fox jumped over the lazy dog"
Solution().toGoatLatin(S)
