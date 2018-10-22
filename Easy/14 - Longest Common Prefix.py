#Method 1:

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if len(strs)==0 or strs[0] =='':
            return ''
        
        if len(strs)==1:
            return(strs[0])
        
        maxstr = ''
        #maxstrf
        #print(maxstr)
        i=0
        j=0
        x= True
        
        while i<=len(strs[0]):
            
            y=[ 1 for item in strs if item[0:i] == maxstr ]
            
            if sum(y)==len(strs):
                i+=1
                j+=1
                maxstr =strs[0][0:j]
            else:
                maxstr=maxstr[:-1]
                break
    

        return maxstr

strs= ["flower","flow","flight"]
#strs = ["dog","racecar","car"]
#strs = ['flick','flirck','fisk']
#strs=['c','c']
#strs=['a','b']
Solution().longestCommonPrefix(strs)
