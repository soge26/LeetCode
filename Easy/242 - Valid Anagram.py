#Method 1:

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s=sorted(s)
        t=sorted(t)
        
        
        if s==t:
            return True
        else:
            return False

s = "anagram"
t = "nagaram"
Solution().isAnagram(s, t)
