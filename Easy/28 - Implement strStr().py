#Method 1:

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        import re
        if len(needle)==0:
            return 0
        x= []
        [x.append(m.start()) for m in re.finditer(needle, haystack)]
        if x:
            return(x[0])
        else:
            return -1

haystack = "hello"
needle = "ll"
#haystack = "aaaaa"
#needle = "bba"
Solution().strStr(haystack, needle)

