import re

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'p':'()','b':'[]','c':'{}'}
        pattern = set(re.findall('.{1,2}', s))

        if pattern.issubset(set(d.values())):
            return True
        else:
            return False





list("()[]{}")[::2]

list("()[]{}")[1::2]

d = {'p':'()','b':'[]','c':'{}'}
set(re.findall('.{1,2}', '()[]{}'))


Solution().isValid('()[]{}')