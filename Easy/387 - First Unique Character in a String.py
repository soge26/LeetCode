#Method 1:

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) == 0:
            return -1
        
        s = list(s)
        strdict = {}

        for i in s:
            
            if i in strdict:
                strdict[i]+=1
            else:
                strdict[i]=1
        
        x = min(strdict.values())
        
        if x != 1:
            return -1
        else:
            for v,j in enumerate(s):
                if strdict[j]==1:
                    return v

s = "leetcode"
s = "loveleetcode"
Solution().firstUniqChar(s)

#Method 2:

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        from collections import defaultdict
        
        sd = defaultdict(int)
        
        for i in s:
            sd[i]+=1
        
        for v,i in enumerate(s):
            if sd[i] == 1:
                return v
        return -1

s = "leetcode"
s = "loveleetcode"
Solution().firstUniqChar(s)
