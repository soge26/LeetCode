#Method 1:

class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        x =s.split(' ')
        for v,i in enumerate(x):
            x[v]= i[::-1]
        return ' '.join(x)

s="Let's take LeetCode contest"
Solution().reverseWords(s)

#Method 2:

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        return ' '.join(reversed(s.split()))[::-1]

s="Let's take LeetCode contest"
Solution().reverseWords(s)
